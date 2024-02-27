brave-instrumentation rationale
Rationale here applies to common decisions made in this directory. See Brave's RATIONALE for internal rationale.

Why does the client response callback run in the invocation context?
This rationale applies equally to CLIENT and PRODUCER spans.

Asynchronous code is often modeled in terms of callbacks. For example, the following pseudo code represents a chain of 3 client calls.

// Assume you are reactive: assembling a call doesn't invoke it.
call = client.call("1")
             .flatMap((r) -> client.call("2"))
             .flatMap((r) -> client.call("3"));

ScopedSpan parent = tracer.startScopedSpan("parent");
try {
  // In reactive style, subscribe attaches the trace context
  call.subscribe(subscriber);
} finally {
  parent.finish();
}
It might be surprising that calls "2" and "3" execute in the "parent" trace context, as opposed to the preceding client call. Put another way, response callbacks run in the invocation context, which cause new spans to appear as as a siblings, as opposed to children of the previous callback (in this case a client).

This may sound unintuitive to those thinking in terms of callback nesting depth, but having a consistent structure allows traces to appear similar regardless of imperative vs async invocation. It also is more easy to reason with, but we'll touch on that later.

Let's consider the above async pseudo code with the logical equivalent in synchronous code. In each case, there are 3 client calls made in sequence. In each case, there's a potential data dependency, but it isn't actually used!
