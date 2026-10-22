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
New Brunswick Route 785: Route 785 is a 68.8 km long mostly north-south secondary highway in the southwestern portion of New Brunswick, Canada.  Locally, this road may be known as either the "Shin Crick Road" or the "Mine Road".  In the early 1980s, a mine was established off Route 785, at Mount Pleasant.  Today, Adex Mining holds a mineral claim on the mine however the mine is currently in an idle state.  As a result of mine development at Mount Pleasant, Route 785 was heavily developed and rerouted from the original stage coach trail.  Another name for the road is the "Sheldon Lee Highway", a satirical reference to former New Brunswick Minister of Transportation, Hon. Sheldon Lee, who continued developed the road during his terms in office, especially on the portion of road north of Mount Pleasant.  Mr. Lee lived in the community of Bonny River, which is located near the southern end of Route 785, and likely many people today, frequently used the Route 785 for travel to Fredericton from the St. George area.  Today, the road is heavily used by forest operations.

Williamson diamond mine: The Williamson Diamond Mine (also known as the Mwadui mine) is a diamond mine 23 km northeast of Shinyanga in Tanzania; it became well known as the first significant diamond mine outside of South Africa.  The mine was established in 1940 by Dr. John Williamson, a Canadian geologist, and has been continuous operation since then, making it one of the oldest continuously operating diamond mines in the world.  Over its lifetime it has produced over 19 million carats (3,800 kg) of diamonds.  The Williamson mine, once owned by its namesake Dr. Williamson and later nationalized by the government of Tanzania.  Since February 2009 the mine is mostly owned by Petra Diamonds, with 75% ownership, the government of Tanzania owning the remaining 25%.

Waykira: Waykira (Aymara "wayku" gorge; mountain brook, "ira" mine, "gorge mine" or "mountain brook mine", also spelled "Huayquera") is a mountain in the Andes of Peru, about 5200 m high.  It is located in the Puno Region, Lampa Province, on the border of the districts Palca and Paratía.  Waykira lies southeast of the mountain Qillqa and south of Hatun Pastu.

Murray Brook Mine: The Murray Brook Mine is a VMS deposit in the Bathurst Mining Camp (BMC) of northern New Brunswick, Canada owned by NovaGold Resources.  The deposit was discovered in 1955 and contains the largest gossan zone in the BMC.  From 1989 to 1992 the gossan zone was processed for gold and silver.  In 1992 copper rich ore was crushed and tested for heap leaching.

Crisson Mine: Crisson Mine was a gold mine in Lumpkin County, Georgia, USA, located just east of Dahlonega.  Like many mines in the area, the property probably started as a placer mine during the Georgia Gold Rush.  Once the placer deposits had been exhausted, an open pit gold mine was established in 1847 and commercial operations continued until the early 1980s.  A small stamp mill was also established here.  Much of the gold used for the gold leaf dome of the Georgia State Capitol was mined at this mine, which was among the most productive mine in the Georgia Gold Belt.  The mine is located just north of the site of the Consolidated Mine, which is itself north of and the Calhoun Mine.

Temagami-Lorrain Mine: Temagami-Lorrain Mine is an abandoned surface and underground mine in Northeastern Ontario, Canada.  It is located about 10 km northeast of the town of Temagami near Sauvé Lake in central Cassels Township.  It is named after the Temagami-Lorrain Mining Company, which carried out work on the property in the early 1900s.

Premier Mine: The Premier Mine is an underground diamond mine owned by Petra Diamonds.  It is situated in the town of Cullinan, 40 km east of Pretoria, Gauteng Province, South Africa.  Established in 1902, it was renamed the Cullinan Diamond Mine in November 2003 in celebration of its centenary.  The mine rose to prominence in 1905, when the Cullinan Diamond — the largest rough diamond of gem quality ever found — was discovered there.  The mine has produced over 750 stones that are greater than 100 carat and more than a quarter of all the world's diamonds that are greater than 400 carat .  It is also the only significant source of blue diamonds in the world.

Mine planter (U.S. Army): Mine planter and the earlier "torpedo planter" was a term used for mine warfare ships into the early days of World War I.  In later terminology, particularly in the United States, a mine planter was a ship specifically designed to install controlled mines or contact mines in coastal fortifications.  This type of ship diverged in both function and design from a ship operating as a naval minelayer.  Though the vessel may be seagoing it is not designed to lay large numbers of mines in open sea.  A mine planter was designed to place controlled minefields in exact locations so that they might be fired individually or as a group from shore when observers noted a target to be at or near a designated mine's position.  The terms and types of specialized ship existed from the 1860s where "torpedoes" were made famous in the American Civil War until the demise of large, fixed coastal fortifications brought on by the changes of World War II.

Northern New Brunswick and Seaboard Railway: The Northern New Brunswick and Seaboard Railway can lay claim to be the railway company with the fewest number of miles of standard gauge track in history.  The province empowered it in 1904 to lay track between Nepisiguit Junction and Grand Falls, a distance of 16 miles, to serve the Drummond Iron Mines, which were discovered in 1897 by William Hussey.  By 1903 the Austin Brook Iron Mine was formed, and operated under the name Drummond until 1913, when went bust.  It was in receivership for some short time until the Dominion Steel and Coal Company purchased the right to operate the mine from Canadian Iron Industries, who held the lease.  Between 1920 and 1926, the construction of the Grand Falls hydroelectricity dam and plant required twice-daily return trips with a steam locomotive.  Thereafter, a gasoline-powered jitney, trolly or automobile with steel wheels would serve until, in the early 1950s the Brunswick Mine attracted attention once again to the area.  In 1955 a highway was pushed through to the mine site, and two years later the rails were sold for scrap.

Ferris-Haggarty Mine Site: The Ferris-Haggerty Mine Site was one of the richest components of the Grand Encampment Mining District in Carbon County, Wyoming.  The site was first exploited by Ed Haggerty, a prospector from Whitehaven, England, in 1897 when he established the Rudefeha Mine on a rich deposit of copper ore.  Haggerty was backed by George Ferris and other investors, of whom all but Ferris dropped out.  The partners sold an interest to Willis George Emerson, who raised investment funding for improvements to the mine.  These facilities included a 16 mi aerial tramway from Grand Encampment over the Continental Divide to the in Encampment.  The mine's assets were eventually acquired by the North American Copper Company for $1 million.  By 1904 the mine had produced $1.4 million in copper ore, and was sold to the Penn-Wyoming Copper Company.  However, even with copper prices peaking in 1907, the company had difficulty making a profit from the remote mine site.  The company was over-capitalized and under-insured and was suffered devastating fires at the mine site in March 1906 and May 1907 which halted production.  Business disputes and a fall in copper prices prevented re-opening of the mine even after it was rebuilt.  Machinery was salvaged after a foreclosure in 1913.  A total of $2 million in copper ore was extracted from the mine during its life.

Question: Which mine was established earlier, Murray Brook Mine or Temagami-Lorrain Mine?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mines_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "mine_name": {
            "type": "string",
            "description": "The name of the mine."
          },
          "establishment_year": {
            "type": "string",
            "description": "The year or period when the mine was established or work began."
          }
        },
        "required": [
          "mine_name",
          "establishment_year"
        ],
        "additionalProperties": false
      },
      "description": "Details of the mines being compared."
    },
    "earlier_mine": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the mine established earlier."
        },
        "establishment_period": {
          "type": "string",
          "description": "The period when the earlier mine was established."
        }
      },
      "required": [
        "name",
        "establishment_period"
      ],
      "additionalProperties": false
    },
    "comparison_summary": {
      "type": "string",
      "description": "A summary statement comparing the establishment dates of the mines."
    }
  },
  "required": [
    "mines_compared",
    "earlier_mine",
    "comparison_summary"
  ],
  "additionalProperties": false
}
