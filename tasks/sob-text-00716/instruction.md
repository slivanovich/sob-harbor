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
Nichols plc: Nichols plc, based in Newton-le-Willows, Merseyside, England, is a company well known for its lead brand Vimto, a fruit flavoured cordial.  The company can trace its roots back to the invention of Vimto, by John Noel Nichols in 1908.  Today the company operates two types of businesses, firstly the sale of Vimto and other brands (such as Panda Pops, which Nichols acquired from Hall & Woodhouse in 2005) via supermarkets and associated outlets throughout the world and secondly its soft drink dispense operation in the UK.  The soft drink operation is handled under the name of Cabana and is the UK's largest independent supplier of dispensed soft drinks.  Due to its success of the Vimto soft drink, Nichols plc started selling Vimto chews and Vimto chew bars.

Marketing in schools: Marketing in schools is a widespread phenomenon in which schools sign contracts allowing certain businesses to conduct marketing activities in school facilities — primarily advertising.  For example, a school might allow only one brand of soft drink to be sold in vending machines on the campus; in return, the soft drink company would provide compensation to the school (frequently money, but it may provide other compensation as well, such as building new facilities or paying for school supplies).  The phrase usually refers to arrangements by elementary schools or high schools, rather than higher education; because this marketing is seen as targeting children, it is very controversial.  One example of this is Channel One News, a TV show, branded as educational, shown in schools that shows two minutes of advertising.  Channel One is shown in over 11,500 middle and high schools across the United States, reaching 7.7 million students.

Rasna: Rasna is a soft drink concentrate brand owned by "Pioma Industries" which is based in Ahmedabad, India.  It was launched in mid-seventies but started gaining popularity in the eighties when the market was dominated by carbonated soft drinks like Thums up, Gold Spot and Limca.  As of 2009, Rasna had a 93% market share in the soft drink concentrate market in India and as of 2011, the company had a turnover of () .

Goombay Punch: Bahamas Goombay Punch is a soft drink that is produced in the Bahamas.  It is very sweet and has a high sugar content.  Goombay Punch is widely available throughout the bahamas in 12 fl oz cans as well as 20 fl oz bottles.  6-packs of the soft drink are also widely available.  The soft drink comes in two varieties, Bahamas Goombay Punch (the stock flavor) and Goombay Fruit Champagne.  The regular flavor is yellow in color (see picture).

Piscola: Piscola or Combinado Nacional (national mix) is a highball cocktail, made of pisco and most commonly a cola drink, that is popular in Chile.  A piscola may be "black" or "white" depending if it is mixed with a cola or ginger ale, Tonic, Sprite or a similar soft drink.  The drink is prepared by filling a highball glass with ice and then adding pisco followed by the soft drink in a proportion ranging from 1:1 to 1:3.  Sometimes slices of lemon or key lime may be added.  In Chile, February 8 has been celebrated as the "day of the piscola" since 2003.

Sunkist (soft drink): Sunkist is a brand of primarily orange flavored soft drinks launched in 1979.

Harry Roberts (inventor): Harry Roberts is the co-inventor of julmust and co-founder of Roberts AB in Örebro in 1910, Sweden.  After studying chemistry in Germany during the late 19th century he invented the soft drink together with his father Robert Roberts.

Julmust: Julmust (Swedish: "jul" "Yule" and "must " "not yet fermented juice of fruit or berries", though there is no such juice in "julmust") is a soft drink that is mainly consumed in Sweden around Christmas.  During the other part of the year it is usually quite difficult to find in stores, but sometimes it is sold at other times of the year under the name "must".  At Easter the name is påskmust (from "påsk ", "Easter" / "Paschal" ["q.v."]).  The content is the same regardless of the marketing name, although the length of time it is stored before bottling differs; however, the beverage is more closely associated with Christmas, somewhat less with Easter and traditionally not at all with the summer.  45 million litres of "julmust" are consumed during December, which is around 50% of the total soft drink volume in December and 75% of the total yearly must sales.

Shasta (soft drink): Shasta Beverages is an American soft drink manufacturer which markets a value priced soft drink line with a wide variety of soda flavors under the brand name Shasta Soda.  The company name is derived from Mount Shasta and an associated spring.

Roberts AB: Roberts AB is the company that makes the syrup for the traditional Swedish drink julmust.  The company was founded in 1910 by Harry Roberts and his father Robert Roberts (who died in 1932).  The company is located in Örebro, Sweden and currently has 15 employees.  The current owner is Göran Roberts, a grandson of Harry.  They do not produce their own soft drinks, just the syrup.  Apart from julmust they also make syrup for cola, various fruit drinks and Champis.

Question: Which soft drink is primarily associated with Christmas, Sunkist or Julmust?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "soft_drink_name": {
      "type": "string",
      "description": "The name of the soft drink primarily associated with Christmas."
    },
    "primary_association": {
      "type": "string",
      "description": "The holiday or event the soft drink is primarily associated with."
    },
    "country_of_consumption": {
      "type": "string",
      "description": "The country where the soft drink is mainly consumed during its associated period."
    },
    "consumption_details": {
      "type": "object",
      "properties": {
        "monthly_volume_liters": {
          "type": "integer",
          "description": "The volume of the soft drink consumed during the associated month, in liters."
        },
        "percentage_of_total_soft_drink_volume_in_month": {
          "type": "number",
          "description": "The percentage of the total soft drink volume in the associated month that this drink accounts for."
        },
        "percentage_of_total_yearly_sales": {
          "type": "number",
          "description": "The percentage of the total yearly sales of this specific drink that occurs during the associated month."
        }
      },
      "required": [
        "monthly_volume_liters",
        "percentage_of_total_soft_drink_volume_in_month",
        "percentage_of_total_yearly_sales"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "soft_drink_name",
    "primary_association",
    "country_of_consumption",
    "consumption_details"
  ],
  "additionalProperties": false
}
