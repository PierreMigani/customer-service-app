import React, { useState } from 'react';
import axios from 'axios';

function EmailCategorizer() {
  const [emailText, setEmailText] = useState('');
  const [category, setCategory] = useState('');

  const handleEmailChange = (e) => {
    setEmailText(e.target.value);
  };

  const categorizeEmail = async () => {
    try {
      const response = await axios.post('http://localhost:5000/categorize', { text: emailText });
      setCategory(response.data.category);
    } catch (error) {
      console.error("There was an error categorizing the email!", error);
    }
  };

  return (
    <div>
      <textarea value={emailText} onChange={handleEmailChange} />
      <button onClick={categorizeEmail}>Categorize</button>
      {category && <p>Category: {category}</p>}
    </div>
  );
}

export default EmailCategorizer;
