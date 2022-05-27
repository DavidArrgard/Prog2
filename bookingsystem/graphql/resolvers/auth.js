const bcrypt = require("bcryptjs");
const User = require("../../models/users");
const jwt = require("jsonwebtoken");

module.exports = {
  createUser: async (args) => {
    //Skaper Användare
    try {
      const existingUser = await User.findOne({ email: args.userInput.email });
      if (existingUser) {
        throw new Error("Users email taken!!!");
      }
      const hashedPass = await bcrypt.hash(args.userInput.password, 12);
      const user = new User({
        email: args.userInput.email,
        password: hashedPass,
      });
      const result = await user.save();

      return { ...result._doc, password: null, _id: result.id };
    } catch (err) {
      throw err;
    }
  },
  login: async ({ email, password }) => {
    const user = await User.findOne({ email: email });
    if (!user) {
      throw new Error("User not found!!!");
    }
    const isEqual = await bcrypt.compare(password, user.password);
    if (!isEqual) {
      throw new Error("Password is incorrect!!");
    }
    const token = jwt.sign(
      { userId: user.id, email: user.email },
      "superhemligtoken",
      {
        expiresIn: "1h",
      }
    );
    return { userId: user.id, token: token, tokenExpiration: 1 };
  },
};
