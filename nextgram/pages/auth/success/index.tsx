import { useEffect } from "react";
import axios from "axios";

function LoginSuccess() {
  // get query parameter from the URL
  useEffect(() => {
    const query = new URLSearchParams(window.location.search);
    const code = query.get("code");
    const state = query.get("state");

    console.log(code, state);

    const config = {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    };

    const details = {
      code: code,
      state: state,
    };

    const formBody = Object.keys(details)
      .map(
        (key) =>
          encodeURIComponent(key) + "=" + encodeURIComponent(details[key])
      )
      .join("&");

    console.log(formBody);

    // axios
    //   .post(`http:localhost:8000/api/oauth/o/github/?${formBody}`, config)
    //   .then((response) => {
    //     console.log(response);
    //   })
    //   .catch((err) => console.log(err));
  }, []);

  return <div>Congratulations! Login was successful</div>;
}

export default LoginSuccess;
