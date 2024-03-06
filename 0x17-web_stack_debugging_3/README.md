# Web stack debugging #3

Sometimes logs aren't enough, when debugging. Either because the error isn't being logged, or because the logs aren't providing enough information. When this happens, it's time to go down the stack.

This Repo's task is to debug a WordPress website running on the usual LAMP stack. WordPress is a very popular tool, in fact 810 million websites use it, that's 43% of all the websites on the internet.

### Debugging Process

- Using strace, find out why Apache is returning a 500 error.
- Fix it.
- Automate it using Puppet.
