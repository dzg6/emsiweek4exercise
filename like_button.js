'use strict';
function getData(e) {
  console.log(e.target.id)

//   const request = new Request('http://localhost:5000/fruits');
//   fetch(request)
//   .then(response => response.json())
//   .then(data => {
//     console.log('Success:', data);
//   })
//   .catch((error) => {
//     console.error('Error:', error);
//   });
}

// const e = React.createElement;

// class LikeButton extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = { liked: false };
//   }

//   render() {
//     if (this.state.liked) {
//       return 'You liked comment number ' + this.props.commentID;
//     }

//     return e(
//       'button',
//       { onClick: (e) => getData(e) },
//       'Fruits'
//     );
//   }
// }


class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return (
      <button onClick={() => this.setState({ liked: true }) }>
        Like
      </button>
    );
  }
}

let domContainer = document.querySelector('#like_button_container');
ReactDOM.render(<LikeButton />, domContainer);

// const element = ( <h1>Hello, world!</h1>);

// ReactDOM.render(
//   element,
//   document.getElementsByClassName('like_button_container')
// );


// Find all DOM containers, and render Like buttons into them.
// document.querySelectorAll('.like_button_container')
//   .forEach(domContainer => {
//     ReactDOM.render(
//       e(element),
//       domContainer
//     );
//   });

// // Find all DOM containers, and render Like buttons into them.
// document.querySelectorAll('.like_button_container')
//   .forEach(domContainer => {
//     // Read the comment ID from a data-* attribute.
//     const commentID = parseInt(domContainer.dataset.commentid, 10);
//     ReactDOM.render(
//       e(LikeButton, { commentID: commentID }),
//       domContainer
//     );
//   });