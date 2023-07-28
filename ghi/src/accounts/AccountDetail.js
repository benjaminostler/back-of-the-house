import { Link } from "react-router-dom";

const AccountDetail = ({ accountData }) => {
  return (
    <div className="d-flex flex-row">
      <div className="container-fluid ubody p-3">
        <div className="user-table shadow p-3">
          <h3>Your Account Details</h3>

          <div>
            <p>Username: {accountData && accountData.username}</p>
            <p>Email: {accountData && accountData.email}</p>
            <p>First Name: {accountData && accountData.first_name}</p>
            <p>Last Name: {accountData && accountData.last_name}</p>
            <p>Phone Number: {accountData && accountData.phone_number}</p>
          </div>

          <div>
            <Link to="/editmyaccount">
              <button className="button">
                Edit Account Information
              </button>
            </Link>
          </div>

        </div>
      </div>
    </div>
  );
};
export default AccountDetail;
