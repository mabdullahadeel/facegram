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

    const formBody : string = `code=${encodeURIComponent(details?.code || "")}&state=${encodeURIComponent(details?.state || "")}`


    const url = `http:localhost:8000/api/oauth/o/github/?${formBody}`
    console.log(formBody, " url", url);

    axios
      .post(url, config)
      .then((response) => {
        console.log(response);
      })
      .catch((err) => console.log(err));
  }, []);

  return <div>Congratulations! Login was successful</div>;
}

export default LoginSuccess;
