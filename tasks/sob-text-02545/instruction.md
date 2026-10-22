Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Dividend discount model: The dividend discount model (DDM) is a method of valuing a company's stock price based on the theory that its stock is worth the sum of all of its future dividend payments, discounted back to their present value.  In other words, it is used to value stocks based on the net present value of the future dividends.  The equation most widely used is called the Gordon growth model.  It is named after Myron J. Gordon of the University of Toronto, who originally published it along with Eli Shapiro in 1956 and made reference to it in 1959.  Their work borrowed heavily from the theoretical and mathematical ideas found in John Burr Williams 1938 book "The Theory of Investment Value."

Little Book of Common Sense Investing: The Little Book of Common Sense Investing: The Only Way to Guarantee Your Fair Share of Stock Market Returns is a 2007 book on index investing, by John C. Bogle, the founder and former CEO of the Vanguard Group.  He focuses on index funds, which will give the investor the average market return, and on keeping investing costs low, so that the index fund investor will consistently do better than other investors, after costs.  Trying to beat the market "is a loser's game," according to Bogle and "the more the managers and brokers take, the less investors make."

Equity premium puzzle: The equity premium puzzle refers to the phenomenon that observed returns on stocks over the past century are much higher than returns on government bonds.  It is a term coined by Rajnish Mehra and Edward C. Prescott in 1985, although in 1982 Robert J. Shiller published the first calculation that showed that either a large risk aversion coefficient or counterfactually large consumption variability was required to explain the means and variances of asset returns.  Azeredo (2014) shows, however, that increasing the risk aversion level may produce a negative equity premium in an Arrow-Debreu economy constructed to mimic the persistence in U.S. consumption growth observed in the data since 1929.  Economists expect arbitrage opportunities would reduce the difference in returns on these two investment opportunities to reflect the risk premium investors demand to invest in relatively more risky stocks.

Value premium: In investing, value premium refers to the greater risk-adjusted return of value stocks over growth stocks.  Eugene Fama and K. G. French first identified the premium in 1992, using a measure they called HML (high book-to-market ratio minus low book-to-market ratio) to measure equity returns based on valuation.  Other experts, such as John C. Bogle, have argued that no value premium exists, claiming that Fama and French's research is period dependent.

Option time value: In finance, the time value (TV) ("extrinsic" or "instrumental" value) of an option is the premium a rational investor would pay over its "current" exercise value (intrinsic value), based on the probability it will increase in value before expiry.  For an American option this value is always greater than zero in a fair market, thus an option is "always" worth more than its current exercise value. .  As an option can be thought of as 'price insurance' (e.g., an airline insuring against unexpected soaring fuel costs caused by a hurricane), TV can be thought of as the "risk premium" the option seller charges the buyer—the higher the expected risk (volatility formula_1 time), the higher the premium.  Conversely, TV can be thought of as the price an investor is willing to pay for potential upside.

Sortino ratio: The Sortino ratio measures the risk-adjusted return of an investment asset, portfolio, or strategy.  It is a modification of the Sharpe ratio but penalizes only those returns falling below a user-specified target or required rate of return, while the Sharpe ratio penalizes both upside and downside volatility equally.  Though both ratios measure an investment's risk-adjusted return, they do so in significantly different ways that will frequently lead to differing conclusions as to the true nature of the investment's return-generating efficiency.

John C. Bogle: John Clifton "Jack" Bogle (born May 8, 1929) is an American investor, business magnate, and philanthropist.  He is the founder and retired chief executive of The Vanguard Group.

Investment rating for real estate: An investment rating of a real estate property measures the property’s risk-adjusted returns, relative to a completely risk-free asset.  Mathematically, a property’s investment rating is the return a risk-free asset would have to yield to be termed as good an investment as the property whose rating is being calculated.  The underlying drivers for property ratings are the dividends (net operating income) and capital gains over a certain holding period, and their associated risks or variances.  Similar to other financial ratings developed for mutual funds and stocks, it can be assumed that investors have constant relative risk aversion over the wealth derived from other sources and from their investments.  For simplicity, it can also be assumed that the investment return is not correlated with other sources of wealth but represents 100% of the investor's wealth.  A property’s investment rating is then a transformation of the risk-adjusted averaged return to a single number that conveys the property’s long-term potential to yield profits.

Martin Zweig: Martin Edward Zweig (July 2, 1942 – February 18, 2013) was an American stock investor, investment adviser, and financial analyst.  According to "Forbes" magazine, he was renowned for his "eccentric and lavish lifestyle" as well as having had the most expensive residence in the United States at the time, atop The Pierre on Fifth avenue in Manhattan.  It was listed on the New York City real estate market in 2004 for $70 million and in March 2013 for $125 million.  His particular investing methodology was based on selecting growth stocks that also have certain value characteristics, through a system that uses both fundamental analysis and market timing.  He died in 2013 at the age of 70.

Low-volatility anomaly: The low-volatility anomaly is the observation that portfolios of low-volatility stocks have higher risk-adjusted returns than portfolios with high-volatility stocks in most markets studied.  The capital asset pricing model made some predictions of return versus beta.  First, return should be a linear function of beta, and nothing else.  Also, the return of a stock with average beta should be the average return of stocks (this is easy to show given the first assumption).  Second, the intercept should be equal to the risk-free rate.  Then the slope can be computed from these two points.  Almost immediately these predictions were challenged on the grounds that they are empirically not true.  Studies find that the correct slope is either less than predicted, not significantly different from zero, or even negative.  Also, additional factors are predictive of return independent of beta.

Question: In investing, value premium refers to the greater risk-adjusted return of value stocks over growth stocks, other experts, such as John Clifton "Jack" Bogle, have argued that no value premium exists, claiming that Fama and French's research is period dependent, Bogle is an investor, business magnate, and philanthropist, of which nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the person."
    },
    "roles": {
      "type": "array",
      "description": "A list of roles or professions attributed to the person.",
      "items": {
        "type": "string"
      }
    },
    "related_investment_concept": {
      "type": "string",
      "description": "An investment concept the person is associated with in the context."
    }
  },
  "required": [
    "person_name",
    "nationality",
    "roles",
    "related_investment_concept"
  ],
  "additionalProperties": false
}
