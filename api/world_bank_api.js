import puppeteer from "puppeteer";

const getQuotes = async () => {

  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
  });

  const page = await browser.newPage();

  await page.goto("http://quotes.toscrape.com/", {
    waitUntil: "domcontentloaded",
  });

  const quotes = await page.evaluate(() => {
    const quote = document.querySelector(".quote");

    const text = quote.querySelector(".text").innerText;
    const author = quote.querySelector(".author").innerText;

    return { text, author };
  });

  console.log(quotes);

  await browser.close();
};

getQuotes();