import React, { Component } from 'react';
import Results from './Results.js';
import TweetList from './TweetList.js';
import ImageList from './ImageList.js';
import './App.css';
const axios = require('axios');


class App extends Component{
  //The request
  //axios.get('http://127.0.0.1:5000/yuh').then(res=>(console.log(res)))

  constructor(){
    super();
    this.state = {
      "eventField": "",
      "event": "",
      "isSubmitted": false,
      "ready": true,
      "sentiment": 0,
      "imagesAnalyzed": 0,
      "postsAnalyzed": 0,
      "positivePosts": [],
      "negativePosts": [],
      "imageUrls": [],
      "email": "",
      "university": "UMICH", // Default
      "notRegistered": true,
      "eventReported": false
    }
  }

  handleTextChange = (event) => {
    this.setState({eventField: event.target.value});
  }

  handleEmailChange = (event) => {
    this.setState({email: event.target.value});
  }

  checkEventReported = () => {
    axios.get("http://127.0.0.1:5000/event_status/" + this.state.event)
    .then(res => {
      this.setState({eventReported: res.data.isBad})
    })
  }

  handleUniversity = (event) => {
    this.setState({university: event.target.value})
  }

  badEvent = (event) => {
    event.preventDefault();
    axios.post("http://127.0.0.1:5000/send_report_emails", {
      event: this.state.event,
      university: this.state.university
    })

    alert("Thank you for notifying us!");
    this.setState({eventReported: true})
  }

  registerUser = (event) => {
    event.preventDefault();
    axios.post("http://127.0.0.1:5000/enroll_user", {
      email: this.state.email,
      university: this.state.university
    })

    console.log("Register user, email: " + this.state.email + ", university: " + this.state.university);
    this.setState({notRegistered: false})
  }

  handleSubmit = (event) => {
    //API call goes here
    event.preventDefault();
    this.setState({ready: false})
    this.setState({event: this.state.eventField})
    this.setState({isSubmitted: true});
    axios.get('http://127.0.0.1:5000/' + this.state.eventField)
      .then(res => {
        console.log(res)
        this.setState({imagesAnalyzed: res.data.imagesAnalyzed})
        this.setState({postsAnalyzed: res.data.postsAnalyzed})
        this.setState({sentiment: res.data.sentiment})
        this.setState({positivePosts: res.data.positivePosts})
        this.setState({negativePosts: res.data.negativePosts})
        this.setState({imageUrls: res.data.urls})
        this.setState({ready: true})
      })
      .catch(err => {
        console.log(err);
        this.setState({isSubmitted: false})        
      })
  }

  render(){
    if (this.state.isSubmitted === false){
      return (
        <div className="App">
          <h1 className="SentiGo">SentiGo</h1>
          <form onSubmit={this.handleSubmit}>
            <label>
              <input className="search" type="text" name="text" placeholder="Event Name" onChange={this.handleTextChange} />
            </label>
          </form>

        </div>
      );
    }
    else if (this.state.ready === false){
      return (
        <div className="App">
          <h1> Loading results... </h1>
        </div>
        );
    }
    else{
      this.checkEventReported();
      return (
        <div className="App">
          <Results imagesAnalyzed={this.state.imagesAnalyzed} postsAnalyzed={this.state.postsAnalyzed}
           sentiment={this.state.sentiment} event={this.state.event} eventReported={this.state.eventReported}
           notRegistered={this.state.notRegistered} badEvent={this.badEvent} ></Results>
           <br></br>

          <div className="col">
            <TweetList tweetArray={this.state.positivePosts} categoryName='Positive'></TweetList>
            <TweetList tweetArray={this.state.negativePosts} categoryName='Negative'></TweetList>
          </div>
          
          <br></br>
          <ImageList urlList={this.state.imageUrls}></ImageList>
          <br></br>
          
          <br></br>
          <form onSubmit={this.handleSubmit}>
              <label>
                <input className="search" placeholder="Search For Another Event" type="text" name="text" onChange={this.handleTextChange} />
              </label>
            </form>
            <br></br>
            <br></br>
          
          <br></br>
          {this.state.notRegistered ? (
          <form onSubmit={this.registerUser}>
            Register For Notifications {` `} 
            <label>
              <input type="text" name="text" placeholder="Email Address" onChange={this.handleEmailChange} />
            </label>
            {` `}
            <select value={this.state.university} onChange={this.handleUniversity} >
              <option value="UMICH">University of Michigan</option>
              <option value="MSU">Michigan State University</option>
            </select>
            {` `}
            <input type="submit" value="Submit" />
          </form>
          ) : ( 
            <div></div>
          )}

        </div>
      );
    }

  }
}

export default App;
