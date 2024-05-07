import React, { useState } from "react";

export default function MenuItemForm() {
  const [category, setCategory] = useState("");
  const [name, setName] = useState("");
  const [picture_url, setPictureUrl] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {
      category,
      name,
      picture_url,
      description,
      price,
    };
    const menuItemUrl = `${process.env.REACT_APP_API_HOST}/menu_items/`;
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(menuItemUrl, fetchConfig);
    if (response.ok) {
      const newMenuItem = await response.json();
      console.log("new menu Item", newMenuItem);

      setCategory("");
      setName("");
      setPictureUrl("");
      setDescription("");
      setPrice("");
      window.location.reload();
    }
  };

  const handleCategoryChange = (event) => {
    setCategory(event.target.value);
  };
  const handleNameChange = (event) => {
    setName(event.target.value);
  };
  const handlePictureUrlChange = (event) => {
    setPictureUrl(event.target.value);
  };
  const handleDescriptionChange = (event) => {
    setDescription(event.target.value);
  };
  const handlePriceChange = (event) => {
    setPrice(event.target.value);
  };

  return (
    <>
      <div className="row">
        <div className="offset-3 col-6">
          <div className="shadow p-4 mt-4">
            <h1>Create a menu item</h1>
            <form
              onSubmit={handleSubmit}
              id="create-menu-item-form"
            >
              <div className="form-floating mb-3">
                <input
                  onChange={handleCategoryChange}
                  placeholder="Category"
                  required
                  value={category}
                  type="text"
                  name="category"
                  id="category"
                  className="form-control"
                />
                <label htmlFor="category">Category</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  onChange={handleNameChange}
                  placeholder="Menu Item Name"
                  required
                  value={name}
                  type="text"
                  name="name"
                  id="name"
                  className="form-control"
                />
                <label htmlFor="name">Name</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  onChange={handlePictureUrlChange}
                  placeholder="Picture Url"
                  required
                  value={picture_url}
                  type="text"
                  name="picture_url"
                  id="picture_url"
                  className="form-control"
                />
                <label htmlFor="picture_url">Picture Url</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  onChange={handleDescriptionChange}
                  placeholder="Description"
                  required
                  value={description}
                  type="text"
                  name="description"
                  id="description"
                  className="form-control"
                />
                <label htmlFor="description">Description</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  onChange={handlePriceChange}
                  placeholder="Price"
                  required
                  value={price}
                  type="text"
                  name="price"
                  id="price"
                  className="form-control"
                />
                <label htmlFor="price">Price</label>
              </div>
              <button type="submit" className="btn btn-outline-primary">
                Create
              </button>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}
