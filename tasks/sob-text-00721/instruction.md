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
Robert Burnes: Robert Burnes or Robert Burness (1719-1789) was an uncle of the poet Robert Burns on his father's side, who left the family farm of Clochnahill or Clokenhill in Kincardineshire with his younger brother William Burnes.  He found work at the Lochridge or Lochrig limestone quarries and lime kilns that lay near Byrehill Farm near Stewarton.  He may have been a gardener later a teacher and then a land steward on the nearby Robertland Estate.  Robert Burns referred to his relation as "Poor Uncle Robert".

James Donn: James Donn (1758–1813) was an English botanist and gardener.  He was trained by William Aiton, a protege of Sir Joseph Banks and was Curator of the Cambridge University Botanic Gardens, Cambridge, from 1790 until his death.  His most important work was "Hortus Cantabrigiensis", first published in 1796 but with several later, much expanded, editions.  It carried on past his death until 1845.

John Tradescant the Elder: John Tradescant the Elder ( ; c. 1570s – 15–16 April 1638), father of John Tradescant the younger, was an English naturalist, gardener, collector and traveller, probably born in Suffolk, England.  He began his career as head gardener to Robert Cecil, 1st Earl of Salisbury at Hatfield House, who initiated Tradescant in travelling by sending him to the Low Countries for fruit trees in 1610/11.  He was kept on by Robert's son William, to produce gardens at the family's London house, Salisbury House.  He then designed gardens on the site of St Augustine's Abbey for Edward Lord Wotton in 1615-23.

William Tricker: William Tricker (1852–1916) was an English-born estate gardener.  He trained at Kew Gardens in London, before emigrating to the United States in the later 19th century.  His interest was in aquatic plants, and he began a company, named William Tricker, that specialized in aquatic plants.  The company sent out its first mail order catalog in 1892, and is still operating, as William Tricker, Inc. based in Independence, Ohio.  The company currently displays Tricker's original catalog.  Being a plantsman, he wrote many articles for the publication "Garden and Forest" in the 1890s dealing with aquatic plants.  He is well known for producing many hybrid water lilies that are still known around the world.  He introduced a water lily with 6-feet pads from South America, which he named "Victoria trickeri", although it is now known as "Victoria cruziana".  He died in 1916, after which his son, Charles Tricker, took over the business.

William Carlos Williams (band): William Carlos Williams are an Atlanta-based jazz group with Death Metal influences.  The five-man group was founded by Stewart Voegtlin, Wes Daniel and Rob Parham.  Gold Sparkle Band saxophonist Rob Mallard and Andrew Burnes joined shortly after in 1995.  The group released two albums, "White Women" (1997) and "Collection Plate" (1998).

Inverugie Castle: Inverugie Castle or Cheyne's Tower is the ruins of a motte-and-bailey castle in Aberdeenshire, Scotland.

James Gordon (botanist): James Gordon (1708–1780) was a gardener who became a nurseryman, and later a seed merchant in London, specializing in exotics such as camellia and rhododendron; he is also credited with the introduction of the American Elm, "Ulmus americana", in 1752. Appointed gardener to James Sherard at Eltham in 1730, he progressed to Lord Petre's estate at Thorndon Hall, Essex, in 1738 before starting a nursery at Mile End in 1742, later moving to Bow, and establishing a seed shop at Thistle & Crown, 25 Fenchurch Street.  His sons, William, James, and Alexander, assumed control of the nursery in 1776.  Although a correspondent of Linnaeus, he never wrote works of his own.  "He had more knowledge in vegetation than all the gardeners and writers in England put together, but is too modest to publish anything" He died at Barking, Essex, on 20 December 1780.

William Burnes: William Burnes or William Burness (11 November 1721 – 13 February 1784), the father of Robert Burns the poet, was born at either Upper Kinmonth or Clochnahill Farm, Dunnottar, Kincardineshire, and trained as a gardener at Inverugie Castle, Aberdeenshire, before moving to Ayrshire and becoming a tenant farmer.  His parents were Robert Burnes and Isabella Keith.  He retained the spelling 'Burnes' throughout his life, however his son favoured the Ayrshire spelling of 'Burns'.

The Coastal Gardener: The Coastal Gardener, is a weekly thirty-minute nationally, and internationally syndicated award-winning TV series.  The show is seen over Broadcast, cable, satellite and streamed on the World Wide Web.  The Chicago-based Showplace Broadcasting syndicates this now #1 Green, TV Garden Travel Lifestyle series in America, with host, Dave Egbert, that first aired in January 2004.  This series takes viewers “from coast to coast” to display gardens and nurseries exploring plants and ideas for personal gardens all over the country.  A spin-off, "Dave Egbert's Garden Travels" (www.daveegbert.com), began airing in the US and Internationally in January 2009.  The Coastal Gardener is produced by Mark Morro and Big Sur Media, Inc. based in Big Sur, CA and West Plam Beach FL.  Dave Egbert is a garden lecturer and also a writer of numerous newspaper and magazine articles, and a Sunset publish book, "Big Ideas for Small Gardens".  Viewers may also call in and speak with Dave on his weekly coast to coast radio show, Living Green Radio, on the CRN radio network.  (www.crntalk.com)

William Baxter (botanist): William Baxter (died "c." 1836) was an English gardener who collected in Australia on behalf of English nurserymen and private individuals.  He had developed his horticultural reputation as gardener to the Comtesse de Vandes in Bayswater, London, many of the plants he had nurtured being used for illustrations in Curtis’s Botanical Magazine.  He was the first privately financed plant collector to be sent to Australia, his mission being to collect seeds and roots for the London seedsman F. Henchman.

Question: In what country was William Burnes trained as a gardener?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "profession": {
      "type": "string",
      "description": "The profession of the person."
    },
    "training_location_name": {
      "type": "string",
      "description": "The specific place where the person was trained."
    },
    "training_country": {
      "type": "string",
      "description": "The country where the training took place."
    }
  },
  "required": [
    "person_name",
    "profession",
    "training_location_name",
    "training_country"
  ],
  "additionalProperties": false
}
