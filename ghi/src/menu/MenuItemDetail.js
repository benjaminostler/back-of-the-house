import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { addToCart } from "../features/cart/CartSlice";
import { useDispatch } from "react-redux";

export default function MenuItemDetail() {
  const { id } = useParams();
  const [selectedmenuItem, setselectedMenuItem] = useState();
  const dispatch = useDispatch();

  const fetchMenuItemDetail = async () => {
    const url = `${process.env.REACT_APP_API_HOST}/menu_items/ +${id}`;
    const response = await fetch(url);

    if (response.ok) {
      const data = await response.json();
      setselectedMenuItem(data);
    }
  };

  useEffect(() => {
    fetchMenuItemDetail();
  });

  const handleAddToCart = (item) => {
    dispatch(addToCart(item));
  };

  return (
    <>
      {selectedmenuItem ? (
        <div>
          <table>
            <tbody>
              <tr>
                <td>{selectedmenuItem.name}</td>
              </tr>
              <tr>
                <td>
                  <img
                    className="img-thumbail"
                    alt={selectedmenuItem.description}
                    width="200px"
                    height="200px"
                    src={selectedmenuItem.picture_url}
                  />
                </td>
              </tr>
              <tr>
                <td>{selectedmenuItem.description}</td>
              </tr>
              <tr>
                <td>Price: {selectedmenuItem.price}</td>
              </tr>
              <tr>
                <td>
                  <button
                    type="button"
                    className="btn  btn-danger  mx-3"
                    onClick={() => handleAddToCart(selectedmenuItem)}
                  >
                    Add to Cart
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      ) : null}
    </>
  );
}
