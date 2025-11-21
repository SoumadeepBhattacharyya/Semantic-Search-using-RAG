import { useState } from "react";

export default function SearchBox({ setAnswer }) {
  const [query, setQuery] = useState("");

  const search = async () => {
    const res = await fetch(`http://localhost:8000/search?query=${query}`);
    const data = await res.json();
    setAnswer(data.response);
  };

  return (
    <div>
      <input
        placeholder="Ask a question..."
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={search}>Search</button>
    </div>
  );
}
