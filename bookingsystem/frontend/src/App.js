import React, { Component } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import AuthPage from "./pages/Auth";
import BookingsPage from "./pages/Bookings";
import EventsPage from "./pages/Events";
import MainNavigation from "./components/Navigation/MainNavigation";
import AuthContext from "./context/auth-context";

import "./App.css";

// function App() {
//   return (
//     <Router>
//       <header>
//         <MainNavigation />
//       </header>
//       <main className="main-content">
//         <Routes>
//           <Route path="/" element={<Home />} />
//           <Route path="/auth" element={<Auth />} />
//           <Route path="/bookings" element={<Bookings />} />
//           <Route path="/events" element={<Events />} />
//         </Routes>
//       </main>
//     </Router>
//   );
// }

class App extends Component {
  state = {
    token: null,
    userId: null,
  };

  login = (token, userId, tokenExpiration) => {
    this.setState({ token: token, userId: userId });
  };

  logout = () => {
    this.setState({ token: null, userId: null });
  };

  render() {
    return (
      <Router>
        <AuthContext.Provider
          value={{
            token: this.state.token,
            userId: this.state.userId,
            login: this.login,
            logout: this.logout,
          }}
        >
          <MainNavigation />
          <main className="main-content">
            <Routes>
              {!this.state.token && (
                <Route path="/" element={<Navigate to="/auth" replace />} />
              )}
              {!this.state.token && (
                <Route
                  path="/bookings"
                  element={<Navigate to="/auth" replace />}
                />
              )}
              {this.state.token && (
                <Route path="/" element={<Navigate to="/events" replace />} />
              )}
              {this.state.token && (
                <Route
                  path="/auth"
                  element={<Navigate to="/events" replace />}
                />
              )}
              {!this.state.token && (
                <Route path="/auth" element={<AuthPage />} />
              )}
              <Route path="/bookings" element={<BookingsPage />} />
              {this.state.token && (
                <Route path="/events" element={<EventsPage />} />
              )}
            </Routes>
          </main>
        </AuthContext.Provider>
      </Router>
    );
  }
}

export default App;
