import React, { useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";

const Register = () => {
  const navigate = useNavigate();

  const [user, setUser] = useState({
    firstname: "",
    lastname: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleInputs = (e) => {
    let name = e.target.name;
    let value = e.target.value;

    setUser({ ...user, [name]: value });
  };

  const PostData = (
    e,
    firstname,
    lastname,
    email,
    password,
    confirmPassword
  ) => {
    e.preventDefault();

    fetch("http://127.0.0.1:5000/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        firstname,
        lastname,
        email,
        password,
        confirmPassword,
      }),
    })
      .then((res) => res.json())

      .then((data) => {
        console.log(data);
        navigate("/");
      });
  };

  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-12 col-md-7 col-sm-6 ">
          <h1 className="mt-5">Welcome!</h1>
        </div>

        <div className="col-12 col-md-5 col-sm-6">
          <form method="POST">
            <div className="form-group">
              <label htmlFor="username">First Name</label>
              <input
                type="text"
                className="form-control"
                id="firstname"
                name="firstname"
                placeholder="Enter your name"
                value={user.firstname}
                onChange={handleInputs}
              />
            </div>

            <div className="form-group">
              <label htmlFor="username">Last Name</label>
              <input
                type="text"
                className="form-control"
                id="lastname"
                name="lastname"
                placeholder="Enter your name"
                value={user.lastname}
                onChange={handleInputs}
              />
            </div>

            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                className="form-control"
                id="email"
                name="email"
                placeholder="Enter your Email"
                value={user.email}
                onChange={handleInputs}
              />
            </div>

            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                className="form-control"
                id="password"
                name="password"
                placeholder="Enter your Password"
                value={user.password}
                onChange={handleInputs}
              />
            </div>

            <div className="form-group">
              <label htmlFor="cpassword">Confirm password</label>
              <input
                type="password"
                className="form-control"
                id="confirmPassword"
                name="confirmPassword"
                placeholder="Confirm password"
                value={user.confirmPassword}
                onChange={handleInputs}
              />
            </div>
            <NavLink to="http://127.0.0.1:5000/login">
              Already Registered, then Login here!
            </NavLink>
            <br />
            <br />
            <button
              type="submit"
              className="btn btn-primary"
              id="register"
              name="register"
              onClick={PostData}
            >
              Register
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Register;
