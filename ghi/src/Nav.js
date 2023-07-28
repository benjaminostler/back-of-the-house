import { NavLink } from "react-router-dom";
import { useState, useEffect } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";

function Nav() {
  const { token, logout } = useToken();
  const [showLogin, setShowLogin] = useState(true);
  console.log(token);

  // added to pass es linter
  console.log(showLogin);

  const handleLogout = () => {
    logout();
    setShowLogin(true);
    // setShowBanner(true);
  };

  useEffect(() => {
    if (token) {
      setShowLogin(false);
    } else {
      setShowLogin(true);
    }
  }, [token]);

  console.log("Token:", token);

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-success">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">
          Back of the House
        </NavLink>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <NavLink className="nav-link active" aria-current="page" to="/">
                Home
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                className="nav-link active"
                aria-current="page"
                to="/reservations/new"
              >
                Create Reservation
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                className="nav-link active"
                aria-current="page"
                to="/reservations"
              >
                Reservations
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/menu_items">
                Menu Items
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/cart">
                Cart
              </NavLink>
            </li>
            {token && (
              <li className="nav-item">
                <NavLink className="nav-link" to="/orders">
                  Orders
                </NavLink>
              </li>
              )
            }
            {/* Show login and signup links if the user is not logged in */}
            {!token && (
              <>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/loginform">
                    Login
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/signup">
                    Sign-Up
                  </NavLink>
                </li>
              </>
            )}

            {token && (
              <li className="nav-item">
                <NavLink className="nav-link" to="/myaccount">
                  My Account
                </NavLink>
              </li>
            )}

            {/* Show links if the user is logged in */}
            {token && (
              <li className="nav-item">
                <NavLink
                  className="nav-link"
                  value="logout"
                  onClick={handleLogout}
                  to="/"
                >
                  Logout
                </NavLink>
              </li>
            )}

            <li className="nav-item">
              <NavLink className="nav-link" to="menu_items/new">
                Create Menu Item
              </NavLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Nav;
