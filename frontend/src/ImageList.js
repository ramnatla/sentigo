import React from 'react';

const ImageList = ({urlList}) => {
    const headerStyle = {
        'fontWeight': 'bold',
        'textDecoration': 'underline'   
    }

    const imageStyle = {
        'height': '250px',
        'weight': 'auto',
        'padding': '10px'   
    }
    
	if (urlList.length === 0){
		return (
			<div>
                <h1> No Images With Faces Detected </h1>
            </div>
		);
	}
	const display = urlList.map((imgUrl, i) => {
		return (
			<img src={imgUrl} alt={i} key={i} style={imageStyle} />
		);
	});

	return (
		<div className='imageList'>
            <h1 style={headerStyle}>Posts With Images!</h1>
			{display}
		</div>
	);
}

export default ImageList;