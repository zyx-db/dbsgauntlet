import { useEffect, useState } from "react";
import "./App.css";
import io from "socket.io-client";

const socket = io("http://localhost:5000", {
  autoConnect: false,
});

function App() {
  const [token, setToken] = useState("");

  function send_msg() {
    console.log("sending hi");
    socket.emit("message", token);
  }

  const changeToken = (event: any) => {
    setToken(event.target.value);
  };

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
    </>
  );
}

export default App;
