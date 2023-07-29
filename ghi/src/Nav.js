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
            {token && (
              <li className="nav-item dropdown">
                <NavLink
                  className="nav-link dropdown-toggle"
                  to="/"
                  id="navbarDarkDropdownReservationLink"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Reservations
                </NavLink>
                <ul
                  className="dropdown-menu dropdown-menu-dark"
                  aria-labelledby="navbarDarkDropdownReservationLink"
                >
                  <li>
                    <NavLink className="dropdown-item" to="/reservations">
                      Reservation List
                    </NavLink>
                  </li>
                  <li>
                    <NavLink className="dropdown-item" to="/reservations/new">
                      Create Reservation
                    </NavLink>
                  </li>
                </ul>
              </li>
            )}
            {token && (
              <li className="nav-item dropdown">
                <NavLink
                  className="nav-link dropdown-toggle"
                  to="/"
                  id="navbarDarkDropdownMenuLink"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Menu
                </NavLink>
                <ul
                  className="dropdown-menu dropdown-menu-dark"
                  aria-labelledby="navbarDarkDropdownMenuLink"
                >
                  <li>
                    <NavLink className="dropdown-item" to="/menu_items">
                      View Menu
                    </NavLink>
                  </li>
                  <li>
                    <NavLink className="dropdown-item" to="/menu_items/new">
                      Create Menu Item
                    </NavLink>
                  </li>
                </ul>
              </li>
            )}

            {token && (
              <li className="nav-item dropdown">
                <NavLink
                  className="nav-link dropdown-toggle"
                  to="/"
                  id="navbarDarkDropdownMenuLink"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Orders
                </NavLink>
                <ul
                  className="dropdown-menu dropdown-menu-dark"
                  aria-labelledby="navbarDarkDropdownOrdersLink"
                >
                  <li>
                    <NavLink className="dropdown-item" to="/orders">
                      Order History
                    </NavLink>
                  </li>
                  <li>
                    <NavLink className="dropdown-item" to="/orders/new">
                      Create Order
                    </NavLink>
                  </li>
                </ul>
              </li>
            )}
            {token && (
              <li className="nav-item">
                <NavLink className="nav-link active" to="/cart">
                  Cart
                </NavLink>
              </li>
            )}
            
            {!token && (
              <>
                <li className="nav-item">
                  <NavLink className="nav-link active" to="/loginform">
                    Login
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link active" to="/signup">
                    Sign-Up
                  </NavLink>
                </li>
              </>
            )}

            {token && (
              <li className="nav-item">
                <NavLink className="nav-link active" to="/myaccount">
                  My Account
                </NavLink>
              </li>
            )}

            {/* Show links if the user is logged in */}
            {token && (
              <li className="nav-item">
                <NavLink
                  className="nav-link active"
                  value="logout"
                  onClick={handleLogout}
                  to="/"
                >
                  Logout
                </NavLink>
              </li>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Nav;
