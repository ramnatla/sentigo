import React from 'react';

const TweetList = ({tweetArray, categoryName}) => {
    const headerStyle = {
        'fontWeight': 'bold',
        'textDecoration': 'underline'   
	}
	
	const spacingStyle = {
		'width': '50%',
		'padding': '15px' 
    }
    
	if (tweetArray.length === 0){
		return (
			<h1 className='noneFound'>No {categoryName} Tweets Found Yet!</h1>
		);
	}
	const display = tweetArray.map((text, i) => {
		return (
			<h2 key={i}> {text} </h2>
		);
	});

	return (
		<div className='tweetList' style={spacingStyle}>
            <h1 style={headerStyle}>Most {categoryName} Tweets!</h1>
			{display}
		</div>
	);
}

export default TweetList;