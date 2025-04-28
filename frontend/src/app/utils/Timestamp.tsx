import { useEffect, useState } from "react";

export function Timestamp() {
  const [date, setDate] = useState('');

  useEffect(() => {
    setDate(new Date().toLocaleString());
  }, []);

  return <div className="text-sm text-gray-500">{date}</div>;
}