const Event = require("../../models/event");
const Booking = require("../../models/bookings");
const { eventTransformer, bookingTransformer } = require("./merge");

module.exports = {
  bookings: async () => {
    try {
      const bookings = await Booking.find();
      return bookings.map((booking) => {
        return bookingTransformer(booking);
      });
    } catch (err) {
      throw err;
    }
  },
  bookEvent: async (args) => {
    const fetchedEvent = await Event.findOne({ _id: args.eventId });
    const booking = new Booking({
      user: "5c0fbd06c816781c518e4f3e",
      event: fetchedEvent,
    });
    const result = await booking.save();
    return bookingTransformer(result);
  },
  cancelBooking: async (args) => {
    try {
      const booking = await Booking.findById(args.bookingId).populate("event");
      const event = eventTransformer(booking.event);
      await Booking.deleteOne({ _id: args.bookingId });
      return event;
    } catch (err) {
      throw err;
    }
  },
};
