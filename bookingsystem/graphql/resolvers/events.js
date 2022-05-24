const Event = require("../../models/event");
const { eventTransformer } = require("./merge");

module.exports = {
  events: async () => {
    //Skickar ut Events
    try {
      const events = await Event.find();
      return events.map((event) => {
        return eventTransformer(event);
      });
    } catch (err) {
      throw err;
    }
  },
  createEvent: async (args) => {
    //Skapar Events
    const event = new Event({
      title: args.eventInput.title,
      description: args.eventInput.description,
      price: +args.eventInput.price,
      date: new Date(args.eventInput.date),
      creator: "628a413c7021e6603826e2a8", //hårdkodat !!!!!ÄNDRA SEN!!!!!!!!
    });
    let createdEvent;
    try {
      const result = await event.save();
      createdEvent = eventTransformer(result);
      const creator = await User.findById("628a413c7021e6603826e2a8");
      if (!creator) {
        throw new Error("User not found!!!");
      }
      creator.createdEvents.push(event);
      await creator.save();

      return createdEvent;
    } catch (err) {
      console.log(err);
      throw err;
    }
  },
};
