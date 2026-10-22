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
Human trafficking in Costa Rica: Costa Rica is a source, transit, and destination country for women and children subjected to trafficking in persons, specifically forced prostitution.  To a lesser but increasing extent, Costa Rica is a source, transit, and destination country for men, women, and children subjected to conditions of forced labor, particularly in the agriculture, construction, fishing, and domestic service sectors.  Costa Rican women and children are forced into commercial sexual exploitation within the country, and to a limited extent, in Nicaragua and Mexico.  Women and girls from Nicaragua, the Dominican Republic, Guatemala, Colombia, and Panama have been identified in Costa Rica as victims of forced prostitution.  Child sex tourism is a serious problem, particularly in the provinces of Guanacaste, Limon, Puntarenas, and San Jose.  Child sex tourists arrive mostly from the United States, Germany, Sweden, and Italy.  Young men from Nicaragua, Vietnam, China and other Asian countries, are subjected to conditions of forced labor in Costa Rica: during the reporting period, nine Vietnamese men were found in conditions of forced labor in the fishing industry.  Costa Rica serves as a transit point for foreign nationals trafficked to Mexico, Canada, the United States, and Europe.

Human trafficking in Hungary: Hungary is a source, transit, and destination country for women and girls subjected to trafficking in persons, specifically forced prostitution and a source country for men and women in conditions of forced labor.  Women from Hungary are forced into prostitution in the Netherlands, Switzerland, the United Kingdom, Denmark, Germany, Austria, Italy, Spain, Ireland, Greece, and the United States.  Women from eastern Hungary are subjected to forced prostitution in Budapest and areas in Hungary along the Austrian border.  Roma women and girls who grow up in Hungarian orphanages are highly vulnerable to internal forced prostitution.  Men from Western Europe travel to Budapest for the purpose of adult sex tourism, some of which may involve the exploitation of trafficking victims.  Men and women are subjected to conditions of forced labor within Hungary.  Women from Romania and Ukraine are transported through Hungary to the Netherlands, the United Kingdom, Denmark, Germany, Austria, Italy, Switzerland, France, and the United Arab Emirates where they are subsequently subjected to forced prostitution; some of these victims may be exploited in Hungary before they reach their final destination country.

Human trafficking in Guatemala: Guatemala is a source, transit, and destination country for men, women and children subjected to trafficking in persons, specifically sexual servitude and forced labor.  Guatemalan women and children are found in forced prostitution within the country, as well as in Mexico and the United States.  Guatemalan men, women, and children are subjected to forced labor within the country, often in agriculture or domestic service, and particularly near the border with Mexico and in the highland region.  Guatemalan men, women, and children are also found in conditions of forced labor in Mexico and the United States in agriculture and the garment industry.  Indigenous Guatemalans are particularly vulnerable to labor exploitation.  In the Mexican border area, Guatemalan children are exploited for forced begging on streets and forced labor in municipal dumps.  Guatemala is a destination country for women and girls from El Salvador, Honduras, and Nicaragua, in forced prostitution.  Migrants from these Central American countries transit through Guatemala en route to Mexico and the United States; some may become human trafficking victims.  Child sex tourism is a problem in certain tourist areas such as Antigua and Lake Atitlan, and child sex tourists predominately come from Canada, Germany, Spain, and the United States.  The border with Mexico remains a top concern due to the heavy flow of irregular migrants, some of whom are trafficked.

Human trafficking in Malta: Malta is a destination country for European women subjected to trafficking in persons, specifically forced prostitution.  During this reporting period and in the past, the Maltese media also covered possible cases of Maltese teenage girls who may have been involved in forced prostitution in Malta.  Malta is likely a destination country for men subjected to forced labor as reflected by a report in 2009 that three Pakistani males were forced to work in Pakistani restaurants in Malta.  The dozens of children and 4,304 total irregular migrants currently residing in Malta from African countries may be vulnerable to human trafficking in Malta’s “grey” informal labor market.

Øresund Bridge: The Øresund/Öresund/Oresund Bridge (Danish: "Øresundsbroen" , ] ; Swedish: "Öresundsbron" , ] ; hybrid name: "Øresundsbron ") is a combined railway and motorway bridge across the Øresund strait between Sweden and Denmark.  The bridge runs nearly 8 km from the Swedish coast to the artificial island Peberholm in the middle of the strait.  The crossing is completed by the 4 km Drogden Tunnel from Peberholm to the Danish island of Amager.

Human trafficking in Latvia: Latvia is a source and destination country for men and women trafficked for the purposes of commercial sexual exploitation and forced labor.  Latvian women are trafficked to Cyprus, Denmark, Germany, Greece, Italy, the Netherlands, Norway, Spain, and the United Kingdom for commercial sexual exploitation.  Latvian women and teenage girls are also trafficked within the country for the purpose of commercial sexual exploitation.  Men and women from Latvia are trafficked to the United Kingdom for the purpose of forced labor.  In addition, Latvia may be a destination country for victims trafficked from Thailand for the purpose of forced labor.

Human trafficking in Antigua and Barbuda: Antigua and Barbuda is a destination country for a small number of women from Guyana, Haiti, Jamaica, and the Dominican Republic subjected to trafficking in persons, specifically forced prostitution.  To a lesser extent, it is reportedly also a destination country for women subjected to involuntary domestic servitude in private homes.  Business people from the Dominican Republic and Antiguan citizens acting as pimps and brothel owners subject foreign women to forced prostitution primarily in four illegal brothels that operate in Antigua as well as in private residences that operate as brothels.  Some of these foreign women voluntarily migrate to Antigua to engage in prostitution but are subsequently subjected to force or coercion and become victims of sex trafficking.  After their arrival, brothel managers confiscate their passports and threaten the victims with deportation until they repay the brothel owner for travel and other expenses they were not aware they had incurred.  Some other foreign victims of sex trafficking enter the country legally with work permits as “entertainers” then are subsequently forced to engage in prostitution.

Human trafficking in Sierra Leone: Sierra Leone is a source, transit, and destination country for children and women trafficked for the purposes of forced labor and commercial sexual exploitation.  Trafficking within the country is more prevalent than transnational trafficking and the majority of victims are children.  Within the country, women and children are trafficked from rural provinces to towns and mining areas for domestic servitude, sexual exploitation, and forced labor in diamond mines, petty trading, petty crime, and for forced begging.  Women and children may also be trafficked for forced labor in agriculture and the fishing industry.  Transnationally, Sierra Leonean women and children are trafficked to other West African countries, notably Guinea, Côte d'Ivoire, Liberia, Nigeria, Guinea-Bissau, and The Gambia for the same purposes listed above and to North Africa, the Middle East, and Western Europe for domestic servitude and sexual exploitation.  Sierra Leone is a destination country for children trafficked from Nigeria and possibly from Liberia and Guinea for forced begging, forced labor in mines and as porters, and for sexual exploitation.  There have also been cases of children trafficked from refugee communities in Sierra Leone.

Human trafficking in Peru: Peru is a source, transit, and destination country for men, women, and children subjected to trafficking in persons, specifically forced labor and forced prostitution.  Several thousand persons are estimated to be subjected to conditions of forced labor within Peru, mainly in mining, logging, agriculture, brick making, and domestic servitude.  Many trafficking victims are women and girls from impoverished rural regions of the Amazon, recruited and coerced into prostitution in urban nightclubs, bars, and brothels, often through false employment offers or promises of education.  Indigenous persons are particularly vulnerable to debt bondage.  Forced child labor remains a problem, particularly in informal gold mines, cocaine production, and transportation.  There were reports the terrorist group Sendero Luminoso, or Shining Path, recruited children as soldiers and drug mules.  To a lesser extent, Peruvians are subjected to forced prostitution in Ecuador, Spain, Italy, Japan, and the United States, and forced labor in Argentina, Chile, and Brazil.  Peru also is a destination country for some Ecuadorian and Bolivian females in forced prostitution, and some Bolivian citizens in conditions of forced labor.  Child sex tourism is present in Iquitos, Madre de Dios, and Cuzco.  Traffickers reportedly operate with impunity in certain regions where there is little or no government presence.

DSB Øresund: DSB Øresund was a Danish railway company which was the successor of what was left of DSBFirst Denmark.  DSB Øresund operated train services on the tendered Coast Line and half of the train services between Copenhagen Central Station and Malmö via the Øresund Bridge.  The other half of the cross-border service was operated by Transdev.  On 13 December 2015, DSB took over operation of all activities from DSB Orsund A/S.

Question: What is the name of the destination country that can be reached by a bridge that half-operated by Transdev and originates in Sweden?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "destination_country": {
      "type": "string",
      "description": "The name of the destination country."
    },
    "bridge_name": {
      "type": "string",
      "description": "The name of the bridge connecting the countries."
    },
    "bridge_origin_country": {
      "type": "string",
      "description": "The country from which the bridge originates."
    },
    "operating_company": {
      "type": "string",
      "description": "The name of the company that half-operates services on the bridge."
    },
    "connection_types": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Types of connections provided by the bridge (e.g., railway, motorway)."
    }
  },
  "required": [
    "destination_country",
    "bridge_name",
    "bridge_origin_country",
    "operating_company",
    "connection_types"
  ],
  "additionalProperties": false
}
