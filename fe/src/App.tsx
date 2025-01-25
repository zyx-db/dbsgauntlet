import { useEffect, useState } from "react";
import "./App.css";
import io from "socket.io-client";

const socket = io("http://localhost:5000", {
  autoConnect: false,
});

function Chat({messages, updateMessages}) {
  const [currentMessage, setCurrentMessage] = useState("");

  const sendCurrentMessage = () => {
    if (currentMessage.length > 0) {
      updateMessages(currentMessage);
      setCurrentMessage("");
    }
    else {
      console.log("cant send empty");
    }
  };

  return (
    <>
      <div> CHAT </div>
      <ul className="chat-history">
	{messages.map((m, idx) => <li key={idx}> {m} </li>)}
      </ul>
      <input 
	value={currentMessage}
	onChange={(e) => setCurrentMessage(e.target.value)}
	placeholder="enter a msg vro.."
      ></input>
      <button onClick={sendCurrentMessage}>send</button>
    </>
  ) 
}

function App() {
  const [token, setToken] = useState("");
  const [msgs, setMsgs] = useState([]);

  function send_msg() {
    console.log("sending hi");
    socket.emit("message", token);
  }

  const changeToken = (event: any) => {
    setToken(event.target.value);
  };

  const sendMsg = (msg_txt) => {
    setMsgs([...msgs, msg_txt]);
    socket.emit("update_chat", msg_txt);
    console.log('sent ' + msg_txt);
  }

  useEffect(() => {
    socket.connect();
    socket.on("connect", () => {
      console.log("Connected to server");
    });

    socket.on("disconnect", () => {
      console.log("Disconnected from server");
    });

    // Example of sending a message to the server
    socket.emit("message_from_client", "Hello from client");

    // Example of receiving a message from the server
    socket.on("message_from_server", (message) => {
      console.log("Message from server:", message);
    });

    return () => {
      socket.disconnect(); // Clean up on component unmount
    };
  }, []);

  return (
    <>
      <div>db says hi</div>
      <button onClick={send_msg}> click me</button>
      <input onChange={setToken}></input>
      <Chat messages={msgs} updateMessages={sendMsg} />
    </>
  );
}

export default App;
