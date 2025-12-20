import { useState } from 'react';
import './Counter.css';

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div className="counter">
      <h3>Interactive Counter</h3>
      <div className="count-display">{count}</div>
      <div className="button-group">
        <button onClick={() => setCount(count - 1)} className="btn-decrement">
          - Decrease
        </button>
        <button onClick={() => setCount(0)} className="btn-reset">
          Reset
        </button>
        <button onClick={() => setCount(count + 1)} className="btn-increment">
          + Increase
        </button>
      </div>
    </div>
  );
}
