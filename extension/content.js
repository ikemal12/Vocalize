document.addEventListener('click', function(event) {
    const postElement = event.target.closest('.thing');
    if (postElement) {
      const postID = postElement.getAttribute('data-fullname');
      
      if (postID) {
        // Send post ID to the backend
        fetch('http://localhost:5000/get_post_info', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ post_id: postID }),
        })
        .then(response => response.json())
        .then(data => {
          console.log('Title:', data.title);
          console.log('Contents:', data.contents);
        })
        .catch(error => console.error('Error:', error));
      }
    }
  });