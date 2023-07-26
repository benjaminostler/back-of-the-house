import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import MainPage from "./MainPage.js";
import Nav from "./Nav.js";
import SignupForm from "./accounts/SignupForm.js";
import LoginForm from "./accounts/LoginForm.js";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import Menu from "./menu/Menu.js";
import MenuItemDetail from "./menu/MenuItemDetail.js";

function App() {
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, "");

  const [menuItems, setMenuItems] = useState([]);
  // const[selectedmenuItem, setselectedMenuItem]=useState("");

  async function getMenuItems() {
    const url = `http://localhost:8000/menu_items/`;
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      // console.log("menus", data);
      // console.log("data object", data[0]);
      // console.log("!!!!", data[0].picture_url);
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
            <Route path="/menu">
              <Route index element={<Menu menuItems={menuItems} />} />
              {/* <Route path="/{menu_item_id}" OR /:id  element={<MenuItemDetails />} /> */}
              <Route path=":id" element={<MenuItemDetail />} />
            </Route>
          </Routes>
        </div>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
