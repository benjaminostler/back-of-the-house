import React, { useEffect, useState } from "react";


function ReservationForm() {
  const [firstName, setFirstName] = useState("");
  const handleFirstNameChange = (event) => {
    const value = event.target.value;
    setFirstName(value);
  };
  const [lastName, setLastName] = useState("");
  const handleLastNameChange = (event) => {
    const value = event.target.value;
    setLastName(value);
  };
  const [email, setEmail] = useState("");
  const handleEmailChange = (event) => {
    const value = event.target.value;
    setEmail(value);
  };
  const [phoneNumber, setPhoneNumber] = useState("");
  const handlePhoneNumberChange = (event) => {
    const value = event.target.value;
    setPhoneNumber(value);
  };
  const [partySize, setPartySize] = useState("");
  const handlePartySizeChange = (event) => {
    const value = event.target.value;
    setPartySize(value);
  };
  const [date, setDate] = useState("");
  const handleDateChange = (event) => {
    const value = event.target.value;
    setDate(value);
  };
  const [time, setTime] = useState("");
  const handleTimeChange = (event) => {
    const value = event.target.value;
    setTime(value);
  };
  
  const [account, setAccount] = useState(0)
  const handleAccountChange = (event) => {
    const value = event.target.value;
    setAccount(value)
  }
  const [accounts, setAccounts] = useState([])
  const fetchAccountsData = async () => {
    const accountsURL = `${process.env.REACT_APP_API_HOST}/accounts/`
    const response = await fetch(accountsURL)

    if(response.ok) {
        const data = await response.json()
        setAccounts(data)
    }
  }

  useEffect(() => {
    fetchAccountsData()
  }, [])

  const handleSubmit = async (event) => {
    event.preventDefault();
    const date_time = new Date(`${date}T${time}`);
    const reservation = {
      firstName: firstName,
      lastName: lastName,
      email: email,
      phoneNumber: phoneNumber,
      partySize: partySize,
      date_time: date_time,
      account_id: account,
    };

    const reservationURL = `${process.env.REACT_APP_API_HOST}/reservations/`;
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(reservation),
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(reservationURL, fetchConfig);
    if (response.ok) {
      const newReservation = await response.json();
      console.log(newReservation);

      setFirstName("");
      setLastName("");
      setEmail("");
      setPhoneNumber("");
      setPartySize("");
      setDate("");
      setTime("");
      setAccount(0)
    }

  };

    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Create a Reservation</h1>
                    <form onSubmit={handleSubmit} id="create-reservation-form">
                        <div className="form-floating mb-3">
                            <label htmlFor="first_name">First Name:</label>                            
                            <input onChange={handleFirstNameChange} placeholder="First Name" required type="text" name="first_name" id="first_name" className="form-control"/>
                        </div>
                        <div className="form-floating mb-3">
                            <label htmlFor="last_name">Last Name:</label>                            
                            <input onChange={handleLastNameChange} placeholder="Last Name" required type="text" name="last_name" id="last_name" className="form-control"/>
                        </div>
                        <div className="form-floating mb-3">
                            <label htmlFor="email">Email:</label>                            
                            <input onChange={handleEmailChange} placeholder="Email" required type="text" name="email" id="email" className="form-control"/>
                        </div>
                        <div className="form-floating mb-3">
                            <label htmlFor="phone_number">Phone Number:</label>                            
                            <input onChange={handlePhoneNumberChange} placeholder="Phone Number" required type="text" name="phone_number" id="phone_number" className="form-control"/>
                        </div>
                        <div className="mb-3">
                            <label htmlFor="party_size">Party Size:</label>                                   
                            <select onChange={handlePartySizeChange}>
                                {
                                    [...Array(20)].map((_, i) => i + 1)
                                                  .map(i => <option key={i} value={i}>{i}</option>)
                                }
                            </select>
                        </div>
                        <div className="form-floating mb-3">
                            <label htmlFor="date">Date:</label>                            
                            <input value={date} onChange={handleDateChange} placeholder="Date" required type="date" name="date" id="date" className="form-control" />
                        </div>
                        <div className="form-floating mb-3">
                            <label htmlFor="time">Time:</label>                            
                            <input value={time} onChange={handleTimeChange} placeholder="Time" required type="time" name="time" id="time" className="form-control" />
                        </div>
                        <div className="mb-3">
                            <select value={account} onChange={handleAccountChange} required name="account" id="account" className="form-select">
                                <option value="account">Choose your account</option>
                                {accounts.map(account => {
                                    return(
                                        <option key={account.id} value={account.id}>
                                            {account.id}
                                        </option>
                                    );
                                })}
                            </select>
                        </div>                                             
                            <button type="submit" className="btn btn-outline-primary">
                                Create
                            </button>                        
                    </form>
                </div>
            </div>
        </div>
    )
}



export default ReservationForm