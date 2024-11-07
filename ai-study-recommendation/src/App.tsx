import { useState } from 'react'
import Markdown from 'react-markdown'

import './App.css'

function App() {
  const [data, setData] = useState(null);
  const [topic, setTopic] = useState("");


  const handleInput = (event: React.ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value;
    setTopic(value);
  };

  function handleClick() {
    const xhr = new XMLHttpRequest();
    xhr.open(
      'GET', 
      `https://ai-study-recommendation-endpoint-489954815693.us-central1.run.app/get_study_recomendation?topic=%22${topic}%22`);
    xhr.onload = function() {
      if (xhr.status === 200) {
        setData(JSON.parse(xhr.responseText));
      }
    };
    xhr.send();
  }

  return (
    <>
      <h1>Recomendaciones de estudio</h1>
      <div className="card">
        <input placeholder='Ingresa el tema a recomendar' value={topic} onChange={handleInput}/>
        <button onClick={handleClick}>Enviar</button>
        <h2>Gemini recomienda:</h2  ><br/>
        {data ? <div><Markdown>{data}</Markdown></div> : <div>Loading...</div>}
      </div>
    </>
  )
}

export default App
