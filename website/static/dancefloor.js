const ADD_DANCER_URL = '/api/dancefloor/add-dancer'
const POSITION_DANCER_URL = '/api/dancefloor/position-dancer'


class Dancefloor extends React.Component {

  constructor(props) {
    super(props)
    this.video = React.createRef()
    this.me = React.createRef()
    this.container = React.createRef()
    this.state = {
      id: -1,
      video: null,
      offsetTop: -1,
      offsetLeft: -1,
      joining: false,
      recording: false,
      positioning: false,
    }
  }

  recordVideo(again) {
    if (!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia)) {
      alert("Your browser doesn't support video recording — please use Chrome, Firefox, Edge, or Opera.")
      return
    }
    const record = () => {
      navigator.mediaDevices.getUserMedia({
        video: true,
      }).then(stream => {
        this.video.current.srcObject = stream
        this.video.current.play()
        const recorder = new MediaRecorder(stream)
        recorder.onstart = () => {
          setTimeout(() => {
            recorder.stop();
          }, 3 * 1000 + 500);
        }
        recorder.ondataavailable = e => {
          this.video.current.srcObject = null
          const url = URL.createObjectURL(e.data)
          const blob = new Blob([e.data])
          this.setState({video: {url, blob}})
        }
        recorder.start()
      }).catch(error => {
        console.error(error)
      })
    }
    if (again) {
      this.setState({video: null}, record)
    } else {
      this.setState({recording: true}, record)
    }
  }

  positionVideo() {
    fetch(ADD_DANCER_URL, {
       method: 'POST',
       body: this.state.video.blob,
    }).then(response => response.json()).then(data => this.setState({
      id: data.id,
      joining: false,
      recording: false,
      positioning: true,
    }))
  }

  startDragging(e) {
    const startX = e.clientX
    const startY = e.clientY
    console.log(startX, startY)
    window.onmousemove = e => {
      const deltaX = e.clientX - startX
      const deltaY = e.clientY - startY
      console.log(deltaX, deltaY)
      this.me.current.style.setProperty('--x', deltaX + 'px')
      this.me.current.style.setProperty('--y', deltaY + 'px')
    }
    window.onmouseup = e => {
      const box = this.me.current.getBoundingClientRect();
      const x = box.left
      const y = box.top
      const relativeX = x / this.container.current.offsetWidth * 100
      const relativeY = y / this.container.current.offsetHeight * 100
      console.log(relativeX, relativeY)
      this.me.current.style.top = relativeY + '%'
      this.me.current.style.left = relativeX + '%'
      this.me.current.style.setProperty('--x', 0)
      this.me.current.style.setProperty('--y', 0)
      window.onmousemove = null
      window.onmouseup = null
      console.log(this.state.id)
      fetch(POSITION_DANCER_URL, {
        method: 'POST',
        body: JSON.stringify({
          id: this.state.id,
          offset_top: relativeY,
          offset_left: relativeX,
        })
      })
    }
  }

  render() {
    return (
      <div className="dancefloor">
        {this.state.joining && (
          <div className="dancefloor-modal">
            {this.state.recording ?
              (this.state.video ? (
                <div className="dancefloor-start">
                  <button
                    className="dancefloor-button"
                    onClick={() => this.recordVideo(true)}
                  >
                    Record again
                  </button>
                  <div className="dancefloor-video">
                    <video
                      src={this.state.video.url}
                      autoPlay
                      muted
                      loop
                    />
                  </div>
                  <button
                    className="dancefloor-button dancefloor-button1"
                    onClick={() => this.positionVideo()}
                  >
                    Hit the floor!
                  </button>
                </div>
              ) : (
                <div className="dancefloor-video">
                  <video ref={this.video} />
                </div>
              )
            ) : (
              <button
                className="dancefloor-button"
                onClick={() => this.recordVideo()}
              >
                Fire up the camera!
              </button>
            )}
          </div>
        )}
        {this.state.positioning && (
          <div
            className="dancefloor-me"
            onMouseDown={e => this.startDragging(e)}
            ref={this.me}
          >
            <video
              src={this.state.video.url}
              autoPlay
              muted
              loop
            />
          </div>
        )}
        <div ref={this.container} className={`
          dancers
          ${this.state.joining ? 'dancers-blurred' : ''}
        `}>
          {!this.state.positioning && (
            <button
              onClick={() => this.setState({joining: true})}
              className="dancefloor-button dancefloor-join"
            >
              Join the Dancefloor!
            </button>
          )}
          {this.props.dancers.map(dancer => (
            <div
              key={dancer.id}
              className="dancer"
              style={{
                top: dancer.offsetTop + '%',
                left: dancer.offsetLeft + '%',
              }}
            >
              <div className="dancefloor-video">
                <video
                  src={dancer.url}
                  autoPlay
                  muted
                  loop
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    )
  }

}


