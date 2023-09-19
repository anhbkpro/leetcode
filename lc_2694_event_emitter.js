class EventEmitter {
    constructor() {
        this.events = {};
    }

    subscribe(event, cb) {
      this.events[event] = this.events[event] ?? [];
      this.events[event].push(cb);

      return {
        unsubscribe: () => {
          this.events[event] = this.events[event].filter(f => f !== cb);
          //To avoid memory leaks adding a cleanup condition
          if (this.events[event].length === 0) { delete this.events[event] }
        },
      };
    }

    emit(event, args = []) {
        if (!(event in this.events)) return [];
        return this.events[event].map(f => f(...args));
    }
}

const emitter = new EventEmitter();
emitter.emit("firstEvent"); // [], no callback are subscribed yet
emitter.subscribe("firstEvent", function cb1() { return 5; });
emitter.subscribe("firstEvent", function cb2() { return 6; });
console.log(emitter.emit("firstEvent")); // [5, 6], returns the output of cb1 and cb2