class Example extends React.Component {
  
  constructor(props) {
    super(props)
    this.state = {counter: 0}
  }

  render() {
    return (
      <div>
        {this.props.message}
        <br />
        Counter: {this.state.counter}
        <button onClick={() => this.setState({counter: this.state.counter + 1})}>Bump</button>
      </div>
    )
  }

}
