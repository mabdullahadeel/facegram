import { useEffect } from "react";
import axios from "axios";

function LoginSuccess() {
  useEffect(() => {
    const query = new URLSearchParams(window.location.search);
    const code = query.get("code");
    const state = query.get("state");

    const details = {
      code: code,
      state: state,
    };

    const url = "http://127.0.0.1:8000/api/oauth/o/github/";

    console.log(details);

    // axios
    //   .post(url, config)
    //   .then((response) => {
    //     console.log(response);
    //   })
    //   .catch((err) => console.log(err));
    // axios({
    //   method: "post",
    //   url: url,
    //   data: details,
    // })
    //   .then((response) => console.log(response))
    //   .catch((err) => console.log(err));
  }, []);

  return <div>Congratulations! Login was successful</div>;
}

export default LoginSuccess;
