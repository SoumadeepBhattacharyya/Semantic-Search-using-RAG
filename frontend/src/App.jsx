import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const search = async () => {
    if (!query.trim()) return;
    setLoading(true);

    try {
      const res = await fetch("http://localhost:5000/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center p-6">
      <h1 className="text-4xl font-bold my-6">🔍 Semantic Search using RAG</h1>

      <div className="w-full max-w-xl flex gap-2">
        <input
          type="text"
          className="w-full p-3 rounded bg-gray-800 border border-gray-700"
          placeholder="Ask anything..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button
          onClick={search}
          className="px-6 py-3 bg-blue-600 rounded hover:bg-blue-700"
        >
          Search
        </button>
      </div>

      {loading && (
        <p className="mt-6 animate-pulse text-gray-400">Searching...</p>
      )}

      {result && (
        <div className="mt-6 w-full max-w-2xl bg-gray-800 p-4 rounded">
          <h2 className="text-xl font-semibold mb-2">Result</h2>
          <p className="text-gray-300">{result.answer}</p>

          {result.sources?.length > 0 && (
            <div className="mt-4">
              <h3 className="font-semibold">Sources:</h3>
              <ul className="list-disc ml-6 text-gray-400">
                {result.sources.map((src, idx) => (
                  <li key={idx}>{src}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
