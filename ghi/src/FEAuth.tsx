import React, {
  createContext,
  Dispatch,
  ReactNode,
  SetStateAction,
  useContext,
  useEffect,
  useState,
} from "react";

interface LoginInterface {
  username: string;
  password: string;
}

type RegistrationData = LoginInterface | any;

export const getToken = async (baseUrl: string): Promise<string> => {
  return fetch(`${baseUrl}/token`, {
    credentials: "include",
  })
    .then((response: Response) => response.json())
    .then((data) => data?.access_token ?? null)
    .catch(console.error);
};

export type AuthContextType = {
  token: string | null;
  setToken: Dispatch<SetStateAction<string | null>>;
  baseUrl: string;
};

export const AuthContext = createContext<AuthContextType>({
  token: null,
  setToken: () => null,
  baseUrl: "",
});

interface AuthProviderProps {
  children: ReactNode;
  baseUrl: string;
}

export const AuthProvider = (props: AuthProviderProps) => {
  const [token, setToken] = useState<string | null>(null);
  const { children, baseUrl } = props;

  return (
    <AuthContext.Provider value={{ token, setToken, baseUrl }}>
      <TokenNode />
      {children}
    </AuthContext.Provider>
  );
};

export const useAuthContext = () => useContext(AuthContext);

const useToken = () => {
  const { token, setToken, baseUrl } = useAuthContext();

  useEffect(() => {
    const fetchToken = async () => {
      const token = await getToken(baseUrl);
      setToken(token);
    };
    if (!token) {
      fetchToken();
    }
  }, [setToken]);

  const logout = async () => {
    if (token) {
      const url = `${baseUrl}/token`;
      fetch(url, { method: "delete", credentials: "include" })
        .then(() => {
          setToken(null);
          // Delete old token
          document.cookie =
            "fastapi_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        })
        .catch(console.error);
    }
  };

  const login = async (username: string, password: string) => {
    const url = `${baseUrl}/token`;
    const form = new FormData();
    form.append("username", username);
    form.append("password", password);
    fetch(url, {
      method: "post",
      credentials: "include",
      body: form,
    })
      .then(() => getToken(baseUrl))
      .then((token: string | null) => {
        if (token) {
          setToken(token);
        } else {
          throw new Error(`Failed to get token after login. Got ${token}`);
        }
      })
      .catch(console.error);
  };

  const register = async (
    userData: RegistrationData,
    url: string,
    method = "POST"
  ) => {
    fetch(url, {
      method: method,
      body: JSON.stringify(userData),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then(() => login(userData.username, userData.password))
      .catch(console.error);
  };

  const fetchWithCookie = async (
    url: string,
    method = "GET",
    options: object = {}
  ): Promise<any> => {
    return fetch(url, {
      method: method,
      credentials: "include",
      ...options,
    })
      .then((resp: Response) => resp.json())
      .catch(console.error);
  };

  const fetchWithToken = async (
    url: string,
    method = "GET",
    otherHeaders: object = {},
    options: object = {}
  ): Promise<any> => {
    return fetch(url, {
      method: method,
      headers: { Authorization: `Bearer ${token}`, ...otherHeaders },
      ...options,
    })
      .then((resp: Response) => resp.json())
      .catch(console.error);
  };

  return { token, register, login, logout, fetchWithCookie, fetchWithToken };
};

export default useToken;

const TokenNode = () => {
  useToken();
  return null;
};
