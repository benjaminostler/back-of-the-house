import { NavLink, useNavigate } from "react-router-dom";
import { useState, useEffect } from 'react';
import useToken from '@galvanize-inc/jwtdown-for-react';


function Nav() {

  const {token, logout} = useToken();
  const [showLogin, setShowLogin] = useState(true);
  console.log(token)

	const handleLogout = () => {
		logout();
		setShowLogin(true);
    // setShowBanner(true);
	};

	const checkForToken = () => {
		if (token) {
			setShowLogin(false);
		} else {
      setShowLogin(true);
    }
	};

	useEffect(() => {
		checkForToken();
	}, [token]);

  console.log('Token:', token);


  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-success">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">
          Gastronauts
        </NavLink>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <NavLink className="nav-link active" aria-current="page" to="/">
                Home
              </NavLink>
            </li>

            {/* Show login and signup links if the user is not logged in */}
            {!token && (
              <>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/loginform">
                    Login
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/accounts/new">
                    Sign-Up
                  </NavLink>
                </li>
              </>
            )}

            {/* Show the logout link if the user is logged in */}
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
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Nav;
