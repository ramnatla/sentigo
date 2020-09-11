import React from 'react';

const Results = ({postsAnalyzed, imagesAnalyzed, sentiment, event, eventReported, notRegistered, badEvent}) => {

	if (sentiment === "no data"){
		return (
			<h1>No Data Found</h1>
		);
	}

	let recommendation = "UNSAFE"
	let recStyle = {
		'color': 'red'
	}

	if (sentiment > 0.1){
		recommendation = "SAFE"
		recStyle = {
			'color': '#3CFF00'
		}
	}
	else if (sentiment >= -0.1){
		recommendation = "NEUTRAL"
		recStyle = {
			'color': 'yellow'
		}
	}

	const bewareStyle = {
        'color': 'red'
	}

	const largerSize = {
        'fontSize': '400%'
	}
	sentiment = sentiment.toFixed(4)

	let beware = <div></div>
	if (eventReported){
		beware = <h2 style={bewareStyle}>
					BEWARE: This event has been reported by another user as being unsafe or uninclusive!
				</h2>
	}

	const reportStyle = {
		'cursor': 'pointer'
	}

	let report = !notRegistered && !eventReported ? (
		<button style={reportStyle} onClick={badEvent}>
		  REPORT EVENT
		</button>
		) : (
		  <div></div>
		)

	return (
		<div>
			<h1 style={largerSize}> {event} </h1>
            <h1> {`This event is `} <span style={recStyle} > {recommendation} </span> {` to attend. By searching ${postsAnalyzed} posts and ${imagesAnalyzed} images,
             we were able to calculate a sentiment analysis of ${sentiment}`} </h1>
			 {beware}
			 {report}
		</div>
	);
}

export default Results;