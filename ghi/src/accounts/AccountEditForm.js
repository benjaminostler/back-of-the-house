import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
// import { UserContext } from "../UserContext";

export default function EditAccount({ currentAccountId, getAccounts }) {
    const [first_name, setFirstName] = useState("");
    const [last_name, setLastName] = useState("");
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [phone_number, setPhoneNumber] = useState("");
    // const { userData } = useContext(UserContext);
    const navigate = useNavigate();

    useEffect(() => {
        fetchAccountDetails();
        getAccounts();
        // eslint-disable-next-line react-hooks/exhaustive-deps
      }, []);

    async function fetchAccountDetails() {
        try {
            const response = await fetch(
                `${process.env.REACT_APP_API_HOST}/accounts/${currentAccountId}/edit`
            );
            if (response.ok) {
                const data = await response.json();
                setFirstName(data.first_name);
                setLastName(data.last_name);
                setUsername(data.username);
                setEmail(data.email);
                setPhoneNumber(data.phone_number);
            } else {
                console.error("Failed to fetch account details");
            }
        } catch (error) {
            console.error("Error while fetching account details")
        }
    }

    const handleFirstnameChange = (event) => {
        const value = event.target.value;
        setFirstName(value);
    };

    const handleLastnameChange = (event) => {
        const value = event.target.value;
        setLastName(value);
    };

    const handleUsernameChange = (event) => {
        const value = event.target.value;
        setUsername(value);
    };

    const handleEmailChange = (event) => {
        const value = event.target.value;
        setEmail(value);
    };

    const handlePhonenumberChange = (event) => {
        const value = event.target.value;
        setPhoneNumber(value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = {
            first_name: first_name,
            last_name: last_name,
            username: username,
            email: email,
            phone_number: phone_number,
        };

        const editUrl = `${process.env.REACT_APP_API_HOST}/accounts/${currentAccountId}`;
        const fetchConfig = {
            method: "PUT",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json",
            },
        };

        try {
            const response = await fetch(editUrl, fetchConfig);
            if (response.ok) {
                getAccounts();
                navigate(`/accounts/${currentAccountId}`);
            } else {
                console.error("Error updating account");
            }
        } catch (e) {
            console.log("Error", e);
        }
    };

    return (
        <div className="card text-bg-light mb-3">
            <h5 className="card-header">Edit Your Account</h5>
            <div className="card-body">
                <form onSubmit={handleSubmit} id="edit-account-form">

                    <div className="form-floating mb-3">
                        <input
                            onChange={handleFirstnameChange}
                            value={first_name}
                            placeholder="first_name"
                            required
                            type="text"
                            id="first_name"
                            className="form-control"
                        />
                        <label htmlFor="first_name">First Name</label>
                    </div>

                    <div className="form-floating mb-3">
                        <input
                            onChange={handleLastnameChange}
                            value={last_name}
                            placeholder="last_name"
                            required
                            type="text"
                            id="last_name"
                            className="form-control"
                        />
                        <label htmlFor="last_name">Last Name</label>
                    </div>

                    <div className="form-floating mb-3">
                        <input
                            onChange={handleUsernameChange}
                            value={username}
                            placeholder="username"
                            required
                            type="text"
                            id="username"
                            className="form-control"
                        />
                        <label htmlFor="username">Userame</label>
                    </div>

                    <div className="form-floating mb-3">
                        <input
                            onChange={handleEmailChange}
                            value={email}
                            placeholder="email"
                            required
                            type="text"
                            id="email"
                            className="form-control"
                        />
                        <label htmlFor="email">Email</label>
                    </div>

                    <div className="form-floating mb-3">
                        <input
                            onChange={handlePhonenumberChange}
                            value={phone_number}
                            placeholder="phone_number"
                            required
                            type="text"
                            id="phone_number"
                            className="form-control"
                        />
                        <label htmlFor="phone_number">Phone Number</label>
                    </div>

                    <button className="btn btn-primary" type="submit">
                        Update Account
                    </button>

                </form>
            </div>
        </div>
    );
};
