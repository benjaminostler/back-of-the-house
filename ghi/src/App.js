import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import MainPage from "./MainPage.js";
import Nav from "./Nav.js";
import SignupForm from "./accounts/SignupForm.js";
import LoginForm from "./accounts/LoginForm.js";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import Menu from "./menu/Menu.js";
// import MenuItemDetails from "./menu/MenuItemDetails.js";
import MenuItemForm from "./menu/MenuItemForm.js";

function App() {
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, "");

  const [menuItems, setMenuItems] = useState([]);
  // const [menuItem, setMenuItem] = useState('');

  async function getMenuItems() {
    const url = "http://localhost:8000/menu_items/";
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setMenuItems(data);
    } else {
      console.error(response);
    }
  }

  useEffect(() => {
    getMenuItems();
  }, []);
  return (
    <BrowserRouter basename={basename}>
      <AuthProvider baseUrl={process.env.REACT_APP_API_HOST}>
        <Nav />
        <div className="container">
          <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/accounts/new" element={<SignupForm />} />
            <Route path="/loginform" element={<LoginForm />} />
            <Route path="menu">
              <Route index element={<Menu menuItems={menuItems}/>}/>
              {/* <Route path="/details" element={<MenuItemDetails menuItems={menuItems} />} /> */}
              <Route path="new" element={<MenuItemForm />} />
            </Route>
          </Routes>
        </div>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
