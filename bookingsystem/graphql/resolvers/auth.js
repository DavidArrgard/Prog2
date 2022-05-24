const bcrypt = require("bcryptjs");
const User = require("../../models/users");

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
        password: hashpass,
      });
      const result = await user.save();

      return { ...result._doc, password: null, _id: result.id };
    } catch (err) {
      throw err;
    }
  },
};
