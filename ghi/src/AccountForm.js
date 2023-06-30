import { useState } from "react";

function BootstrapInput(props) {
  const { id, placeholder, labelText, value, onChange, type } = props;

  return (
    <div className="mb-3">
      <label htmlFor={id} className="form-label">
        {labelText}
      </label>
      <input
        value={value}
        onChange={onChange}
        required
        type={type}
        className="form-control"
        id={id}
        placeholder={placeholder}
      />
    </div>
  );
}

function AccountForm(props) {
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  return (
    <form>
      <BootstrapInput
        id="email"
        placeholder="examplar@example.com"
        labelText="Your email address"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        type="email"
      />
      <BootstrapInput
        id="name"
        placeholder="John Doe"
        labelText="Your name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        type="text"
      />
      <BootstrapInput
        id="password"
        placeholder="Enter password"
        labelText="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        type="password"
      />

      <div className="mb-4">
        <label htmlFor="states" className="form-label">
          Favorite drink?
        </label>
        <select className="form-select" aria-label="Favorite ">
          <option>Choose a drink</option>
          <option value="1">Beer</option>
          <option value="2">Liquor</option>
          <option value="3">Wine</option>
          <option value="4">Coffee</option>
          <option value="5">Soda</option>
          <option value="6">Water</option>
        </select>
      </div>
      <button type="submit" className="btn btn-primary">
        Submit
      </button>
    </form>
  );
}

export default AccountForm;

// before writing in bootstrap component
/*
    <div className="mb-3">
        <label htmlFor="email" className="form-label">
          Email address
        </label>
        <input
          value={email}
          required

          type="email"
          className="form-control"
          id="email"
          placeholder="name@example.com"
        />
      </div>
      <div className="mb-3">
        <label htmlFor="name" className="form-label">
          Name
        </label>
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          type="text"
          className="form-control"
          id="name"
          placeholder="your name here"
        />
      </div>
      <div className="mb-3">
        <label htmlFor="password" className="form-label">
          Password
        </label>
        <input
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          type="password"
          className="form-control"
          id="password"
          placeholder="enter a password"
        />
    </div> */
