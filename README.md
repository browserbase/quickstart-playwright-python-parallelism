<p align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="logo/dark.svg"/>
        <img alt="Browserbase logo" src="logo/light.svg" width="300" />
    </picture>
</p>

<p align="center">
    <a href="https://docs.browserbase.com">Documentation</a>
    <span>&nbsp;·&nbsp;</span>
    <a href="https://www.browserbase.com/playground">Playground</a>
</p>
<br/>

## Parallel Playwright tasks with Browserbase

This repo is a Python template for the [Parallelization Guide](http://docs.browserbase.com/guides/parallelization).


## Setup

### 1. Install dependencies and launch TypeScript in watch mode:

```bash
pip install -r requirements.txt
```


### 2. Get your Browserbase API Key and Project ID:

- [Create an account](https://www.browserbase.com/sign-up) or [log in to Browserbase](https://www.browserbase.com/sign-in)
- Copy your API Key [from your Settings page](https://www.browserbase.com/settings)

### 3. Run the script:

```bash
BROWSERBASE_API_KEY=xxxx python main.py
```


## Further reading

- [See how to leverage the Session Debugger for pip install -r requirements.txt
zsh: command not found: pipfaster development](https://docs.browserbase.com/guides/browser-remote-control#accelerate-your-local-development-with-remote-debugging)
- [Learn more about Browserbase infrastructure](https://docs.browserbase.com/under-the-hood)
- [Explore the Sessions API](https://docs.browserbase.com/api-reference/list-all-sessions)