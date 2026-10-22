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
Bergen: Bergen, historically Bjørgvin, is a city and municipality in Hordaland on the west coast of Norway.  At the end of the first quarter of 2016 , the municipality's population was 278,121, and the Bergen metropolitan region has about 420,000 inhabitants.  Bergen is the second-largest city in Norway.  The municipality covers 465 km2 and is on the peninsula of Bergenshalvøyen.  The city centre and northern neighbourhoods are on Byfjorden, 'the city fjord', and the city is surrounded by mountains; Bergen is known as the 'city of seven mountains'.  Many of the extra-municipal suburbs are on islands.  Bergen is the administrative centre of Hordaland and consists of eight boroughs—Arna, Bergenhus, Fana, Fyllingsdalen, Laksevåg, Ytrebygda, Årstad and Åsane.

Greenstat: Greenstat is a Norwegian company established in 2015.  It works with renewable energy and production and export of hydrogen.  Greenstat claims itself to be "green energy company for a green generation".

Bauer-Nilsen: Bauer Nilsen AS is a Norwegian company established in 1925.

Finance Credit: Finance Credit was a Norwegian company that went bankrupt in 2002, after facing criminal investigation for siphoning funds (in total 1,4 billion NOK) it borrowed from six Norwegian banks to offshore tax havens, in what became known as the Finance Credit scandal, arguably the biggest economic fraud in Norwegian history.  The company was founded by Torgeir Stensrud and Trond Kristoffersen, who were in 2005 convicted on charges of fraud to 7 and 9 years in prison, respectively.  Stensrud and Kristoffersen were also both fined about 100 million €.

SF Norge: SF Norge AS is a Norwegian company for film distribution which was established in 1989.  The company buys and sells films and distributes them to Norwegian cinemas.  On 1 January 2000, SF signed a deal with the American film company 20th Century Fox.  SF has also signed distribution deals with other large companies such as New Line Cinema, MGM and Revolution Studios.

Bug AS: Bug AS is a Norwegian full-service production company established in 1995, By Gunnar Larsen in Bergen, Norway.  In its startup period the company produced industrial 3d, Still Vizualisation and Camera point of view walkthrougs.  Later such as idents for TV commercials and company presentations.

OWEC Tower: OWEC Tower AS is a Norwegian company established in 2004.  They design foundations for offshore wind turbines and are leading within the steel jacket type.

Pickupcat: PickUpCat vas a Norwegian company established in 1996.  The company was based on a module-based concept invented by Norwegian marine engineer Dag O. Aavitsland.  The concept implied that ships should be built in two detachable modules so that the motor module and the cargo module could be separated.

Raufoss Ammunisjonsfabrikker: Raufoss Ammunisjonsfabrikker was a Norwegian company based at Raufoss, established in 1896 as "Rødfoss Patronfabrik".  Initially the company manufactured ammunition, and later also other products, such as aluminium parts to the automotive industry.  Until 1948 the company was a subordinate to the Norwegian Ministry of Defence.  In the 1990s the automobile division was split off as "Raufoss Automotive" and eventually taken over by Norsk Hydro.  The ammunition division was merged with the Swedish company Celsius and the Finnish company Patria, forming the new company Nammo.

Eurofoto: Eurofoto is a Norwegian Online shopping company specializing in Photography products and imaging.  The company is located at Reed, Breim in Gloppen, Sogn og Fjordane.  The company was founded march 7.  2000, and became the leading Norwegian company within online Photography printing and digital imaging.  The company was a daughter company of Intele AS, until September 2010.  Eurofoto AS was then sold to Japan Photo Holding Norge AS.  Their slogan is "Lifelong memories" (no: "Minner for livet")

Question: Bug AS is a Norwegian company established in a city that consists of how many buroughs?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company in question."
    },
    "city_of_establishment": {
      "type": "string",
      "description": "The city where the company was established."
    },
    "number_of_boroughs": {
      "type": "integer",
      "description": "The total number of boroughs in the city of establishment."
    },
    "borough_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the names of the boroughs in the city of establishment."
    }
  },
  "required": [
    "company_name",
    "city_of_establishment",
    "number_of_boroughs",
    "borough_names"
  ],
  "additionalProperties": false
}
