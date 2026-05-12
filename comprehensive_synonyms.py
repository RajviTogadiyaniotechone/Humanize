#!/usr/bin/env python3
"""
Comprehensive Synonym Dictionary for Word Replacement
Expanded word mappings to ensure consistent word changes
"""

# Comprehensive synonym dictionary
COMPREHENSIVE_SYNONYMS = {
    # Academic/Formal Words
    "furthermore": ["also", "plus", "additionally", "moreover", "besides", "what's more", "in addition", "as well", "too", "further"],
    "moreover": ["also", "plus", "additionally", "furthermore", "besides", "what's more", "in addition", "as well", "too", "further"],
    "consequently": ["so", "therefore", "thus", "hence", "as a result", "accordingly", "then", "for this reason", "that's why", "because of this"],
    "nevertheless": ["however", "still", "but", "yet", "even so", "nonetheless", "despite that", "in spite of that", "all the same", "though"],
    "subsequently": ["then", "next", "after", "following", "later", "afterwards", "thereafter", "soon after", "subsequently", "in due course"],
    "accordingly": ["so", "then", "thus", "therefore", "consequently", "as a result", "hence", "for this reason", "that's why", "because of this"],
    "utilize": ["use", "apply", "employ", "work with", "make use of", "put to use", "draw on", "leverage", "harness", "deploy"],
    "facilitate": ["help", "assist", "support", "enable", "make easier", "aid", "promote", "encourage", "simplify", "smooth"],
    "implement": ["start", "begin", "launch", "set up", "put in place", "carry out", "execute", "enact", "apply", "bring about"],
    "optimize": ["improve", "enhance", "boost", "fine-tune", "make better", "perfect", "refine", "upgrade", "maximize", "streamline"],
    "enhance": ["improve", "boost", "upgrade", "strengthen", "make better", "elevate", "heighten", "intensify", "amplify", "enrich"],
    "leverage": ["use", "apply", "employ", "work with", "take advantage of", "make use of", "draw on", "harness", "utilize", "exploit"],
    "establish": ["create", "build", "set up", "form", "start", "found", "initiate", "launch", "begin", "institute"],
    "necessitates": ["requires", "needs", "demands", "calls for", "means", "involves", "entails", "makes necessary", "obligates", "compels"],
    "comprehensive": ["complete", "full", "thorough", "extensive", "detailed", "all-inclusive", "exhaustive", "total", "overall", "inclusive"],
    "subsequent": ["following", "next", "later", "coming", "after", "succeeding", "future", "later on", "afterward", "then"],
    "aforementioned": ["mentioned", "previous", "earlier", "said", "above", "foregoing", "preceding", "cited", "referenced", "noted"],
    "imperative": ["essential", "necessary", "crucial", "vital", "must-have", "required", "obligatory", "compulsory", "indispensable", "critical"],
    "strategic": ["key", "smart", "planned", "important", "thoughtful", "tactical", "calculated", "deliberate", "purposeful", "intentional"],
    "methodologies": ["methods", "approaches", "ways", "techniques", "systems", "procedures", "processes", "strategies", "practices", "protocols"],
    "organizational": ["company", "business", "team", "workplace", "corporate", "organizational", "institutional", "administrative", "managerial", "operational"],
    "infrastructure": ["setup", "system", "structure", "framework", "foundation", "base", "platform", "architecture", "backbone", "skeleton"],
    "various": ["different", "multiple", "several", "many", "diverse", "numerous", "varied", "assorted", "miscellaneous", "various"],
    "factors": ["elements", "aspects", "points", "things", "issues", "components", "variables", "considerations", "features", "characteristics"],
    "technologies": ["tools", "systems", "solutions", "methods", "approaches", "techniques", "platforms", "applications", "software", "hardware"],
    "operational": ["working", "running", "active", "in use", "functional", "operating", "functioning", "live", "ongoing", "current"],
    "efficiency": ["performance", "productivity", "output", "results", "effectiveness", "capability", "competence", "skill", "proficiency", "expertise"],
    "outcomes": ["results", "effects", "consequences", "impacts", "end results", "outputs", "products", "achievements", "findings", "outcomes"],
    "desired": ["wanted", "needed", "required", "targeted", "sought", "preferred", "chosen", "selected", "optimal", "ideal"],
    "competencies": ["skills", "abilities", "strengths", "capabilities", "talents", "competences", "aptitudes", "faculties", "gifts", "qualities"],
    "effectively": ["well", "properly", "successfully", "skillfully", "efficiently", "competently", "proficiently", "adeptly", "capably", "expertly"],
    
    # Common Words
    "must": ["should", "need to", "have to", "ought to", "got to", "must", "required to", "obliged to", "compelled to", "forced to"],
    "should": ["must", "need to", "have to", "ought to", "should", "ought to", "are supposed to", "are expected to", "it's advisable to"],
    "will": ["would", "shall", "going to", "are going to", "will", "intend to", "plan to", "expect to", "are set to"],
    "would": ["will", "shall", "going to", "are going to", "would", "could", "might", "may", "can"],
    "can": ["could", "may", "might", "are able to", "can", "have the ability to", "are capable of", "have the capacity to"],
    "could": ["can", "may", "might", "are able to", "could", "would be able to", "might be able to", "may be able to"],
    "may": ["can", "could", "might", "are able to", "may", "might", "could", "can", "possibly"],
    "might": ["can", "could", "may", "are able to", "might", "may", "could", "can", "possibly"],
    "very": ["extremely", "really", "quite", "highly", "particularly", "especially", "exceptionally", "incredibly", "remarkably", "unusually"],
    "extremely": ["very", "really", "quite", "highly", "particularly", "especially", "exceptionally", "incredibly", "remarkably", "unusually"],
    "really": ["very", "extremely", "quite", "highly", "particularly", "especially", "exceptionally", "incredibly", "remarkably", "unusually"],
    "quite": ["very", "extremely", "really", "highly", "particularly", "especially", "exceptionally", "incredibly", "remarkably", "unusually"],
    "highly": ["very", "extremely", "really", "quite", "particularly", "especially", "exceptionally", "incredibly", "remarkably", "unusually"],
    "particularly": ["very", "extremely", "really", "quite", "highly", "especially", "exceptionally", "incredibly", "remarkably", "unusually"],
    "important": ["key", "crucial", "vital", "essential", "significant", "critical", "major", "principal", "primary", "central"],
    "key": ["important", "crucial", "vital", "essential", "significant", "critical", "major", "principal", "primary", "central"],
    "crucial": ["important", "key", "vital", "essential", "significant", "critical", "major", "principal", "primary", "central"],
    "vital": ["important", "key", "crucial", "essential", "significant", "critical", "major", "principal", "primary", "central"],
    "essential": ["important", "key", "crucial", "vital", "significant", "critical", "major", "principal", "primary", "central"],
    "significant": ["important", "key", "crucial", "vital", "essential", "critical", "major", "principal", "primary", "central"],
    "good": ["great", "excellent", "fine", "nice", "wonderful", "positive", "favorable", "beneficial", "advantageous", "valuable"],
    "great": ["good", "excellent", "fine", "nice", "wonderful", "amazing", "fantastic", "superb", "outstanding", "exceptional"],
    "excellent": ["good", "great", "fine", "nice", "wonderful", "amazing", "fantastic", "superb", "outstanding", "exceptional"],
    "fine": ["good", "great", "excellent", "nice", "wonderful", "acceptable", "satisfactory", "adequate", "decent", "reasonable"],
    "nice": ["good", "great", "excellent", "fine", "wonderful", "pleasant", "agreeable", "delightful", "enjoyable", "charming"],
    "wonderful": ["good", "great", "excellent", "fine", "nice", "amazing", "fantastic", "superb", "outstanding", "exceptional"],
    
    # Size Words
    "big": ["large", "huge", "massive", "enormous", "substantial", "considerable", "significant", "major", "sizeable", "immense"],
    "large": ["big", "huge", "massive", "enormous", "substantial", "considerable", "significant", "major", "sizeable", "immense"],
    "huge": ["big", "large", "massive", "enormous", "substantial", "considerable", "significant", "major", "sizeable", "immense"],
    "massive": ["big", "large", "huge", "enormous", "substantial", "considerable", "significant", "major", "sizeable", "immense"],
    "enormous": ["big", "large", "huge", "massive", "substantial", "considerable", "significant", "major", "sizeable", "immense"],
    "substantial": ["big", "large", "huge", "massive", "enormous", "considerable", "significant", "major", "sizeable", "immense"],
    "small": ["tiny", "little", "minor", "petite", "compact", "minute", "miniature", "diminutive", "microscopic", "minuscule"],
    "tiny": ["small", "little", "minor", "petite", "compact", "minute", "miniature", "diminutive", "microscopic", "minuscule"],
    "little": ["small", "tiny", "minor", "petite", "compact", "minute", "miniature", "diminutive", "microscopic", "minuscule"],
    "minor": ["small", "tiny", "little", "petite", "compact", "minute", "miniature", "diminutive", "microscopic", "minuscule"],
    "petite": ["small", "tiny", "little", "minor", "compact", "minute", "miniature", "diminutive", "microscopic", "minuscule"],
    "compact": ["small", "tiny", "little", "minor", "petite", "minute", "miniature", "diminutive", "microscopic", "minuscule"],
    
    # Speed Words
    "fast": ["quick", "rapid", "swift", "speedy", "hasty", "brisk", "prompt", "immediate", "instant", "sudden"],
    "quick": ["fast", "rapid", "swift", "speedy", "hasty", "brisk", "prompt", "immediate", "instant", "sudden"],
    "rapid": ["fast", "quick", "swift", "speedy", "hasty", "brisk", "prompt", "immediate", "instant", "sudden"],
    "swift": ["fast", "quick", "rapid", "speedy", "hasty", "brisk", "prompt", "immediate", "instant", "sudden"],
    "speedy": ["fast", "quick", "rapid", "swift", "hasty", "brisk", "prompt", "immediate", "instant", "sudden"],
    "hasty": ["fast", "quick", "rapid", "swift", "speedy", "brisk", "prompt", "immediate", "instant", "sudden"],
    "slow": ["sluggish", "gradual", "leisurely", "unhurried", "delayed", "slower", "unhurried", "measured", "steady", "deliberate"],
    "sluggish": ["slow", "gradual", "leisurely", "unhurried", "delayed", "slower", "unhurried", "measured", "steady", "deliberate"],
    "gradual": ["slow", "sluggish", "leisurely", "unhurried", "delayed", "slower", "unhurried", "measured", "steady", "deliberate"],
    "leisurely": ["slow", "sluggish", "gradual", "unhurried", "delayed", "slower", "unhurried", "measured", "steady", "deliberate"],
    "unhurried": ["slow", "sluggish", "gradual", "leisurely", "delayed", "slower", "unhurried", "measured", "steady", "deliberate"],
    "delayed": ["slow", "sluggish", "gradual", "leisurely", "unhurried", "slower", "unhurried", "measured", "steady", "deliberate"],
    
    # Age Words
    "new": ["fresh", "recent", "novel", "modern", "current", "up-to-date", "contemporary", "latest", "brand new", "recently developed"],
    "fresh": ["new", "recent", "novel", "modern", "current", "up-to-date", "contemporary", "latest", "brand new", "recently developed"],
    "recent": ["new", "fresh", "novel", "modern", "current", "up-to-date", "contemporary", "latest", "brand new", "recently developed"],
    "novel": ["new", "fresh", "recent", "modern", "current", "up-to-date", "contemporary", "latest", "brand new", "recently developed"],
    "modern": ["new", "fresh", "recent", "novel", "current", "up-to-date", "contemporary", "latest", "brand new", "recently developed"],
    "current": ["new", "fresh", "recent", "novel", "modern", "up-to-date", "contemporary", "latest", "brand new", "recently developed"],
    "old": ["ancient", "aged", "mature", "vintage", "classic", "outdated", "obsolete", "antiquated", "archaic", "old-fashioned"],
    "ancient": ["old", "aged", "mature", "vintage", "classic", "outdated", "obsolete", "antiquated", "archaic", "old-fashioned"],
    "aged": ["old", "ancient", "mature", "vintage", "classic", "outdated", "obsolete", "antiquated", "archaic", "old-fashioned"],
    "mature": ["old", "ancient", "aged", "vintage", "classic", "outdated", "obsolete", "antiquated", "archaic", "old-fashioned"],
    "vintage": ["old", "ancient", "aged", "mature", "classic", "outdated", "obsolete", "antiquated", "archaic", "old-fashioned"],
    "classic": ["old", "ancient", "aged", "mature", "vintage", "outdated", "obsolete", "antiquated", "archaic", "old-fashioned"],
    
    # Additional Common Words
    "make": ["create", "produce", "generate", "build", "construct", "form", "develop", "manufacture", "fabricate", "assemble"],
    "get": ["obtain", "acquire", "receive", "gain", "secure", "procure", "attain", "achieve", "earn", "collect"],
    "go": ["travel", "move", "proceed", "journey", "head", "advance", "progress", "proceed", "continue", "proceed"],
    "come": ["arrive", "approach", "reach", "enter", "appear", "show up", "present", "emerge", "materialize", "surface"],
    "see": ["observe", "notice", "perceive", "spot", "detect", "identify", "recognize", "discern", "view", "witness"],
    "look": ["gaze", "stare", "glance", "peer", "observe", "view", "watch", "examine", "inspect", "survey"],
    "take": ["grab", "seize", "capture", "hold", "acquire", "obtain", "secure", "get", "receive", "collect"],
    "give": ["provide", "offer", "supply", "deliver", "present", "grant", "bestow", "confer", "award", "furnish"],
    "put": ["place", "set", "position", "locate", "situate", "arrange", "organize", "install", "establish", "deploy"],
    "keep": ["maintain", "preserve", "retain", "hold", "store", "save", "protect", "guard", "secure", "safeguard"],
    "find": ["discover", "locate", "identify", "detect", "uncover", "reveal", "spot", "notice", "perceive", "encounter"],
    "know": ["understand", "comprehend", "realize", "recognize", "perceive", "grasp", "appreciate", "acknowledge", "aware", "conscious"],
    "think": ["believe", "consider", "suppose", "reckon", "assume", "presume", "expect", "feel", "judge", "estimate"],
    "say": ["state", "declare", "announce", "pronounce", "utter", "express", "articulate", "communicate", "convey", "voice"],
    "tell": ["inform", "advise", "notify", "communicate", "explain", "describe", "relate", "report", "announce", "proclaim"],
    "ask": ["inquire", "question", "query", "interrogate", "examine", "investigate", "probe", "explore", "survey", "scrutinize"],
    "work": ["function", "operate", "perform", "run", "execute", "conduct", "carry out", "implement", "apply", "utilize"],
    "seem": ["appear", "look", "seem", "seem", "seem", "seem", "seem", "seem", "seem", "seem"],
    "feel": ["sense", "perceive", "experience", "detect", "notice", "observe", "recognize", "identify", "discern", "apprehend"],
    "try": ["attempt", "endeavor", "strive", "effort", "undertake", "venture", "seek", "aim", "aspire", "pursue"],
    "leave": ["depart", "exit", "go", "withdraw", "retreat", "vacate", "abandon", "desert", "forsake", "quit"],
    "call": ["contact", "phone", "telephone", "dial", "ring", "reach", "communicate", "connect", "get in touch", "call up"],
    "show": ["display", "exhibit", "present", "demonstrate", "reveal", "disclose", "unveil", "expose", "manifest", "illustrate"],
    "change": ["alter", "modify", "adjust", "transform", "convert", "revise", "amend", "adapt", "vary", "shift"],
    "help": ["assist", "aid", "support", "help", "facilitate", "enable", "empower", "encourage", "promote", "foster"],
    "turn": ["rotate", "revolve", "spin", "twist", "pivot", "swerve", "veer", "divert", "change direction", "change course"],
    "start": ["begin", "commence", "initiate", "launch", "kick off", "get underway", "get started", "embark", "set out", "originate"],
    "run": ["operate", "function", "work", "perform", "execute", "conduct", "manage", "administer", "supervise", "oversee"],
    "move": ["shift", "transfer", "relocate", "displace", "reposition", "adjust", "rearrange", "reorganize", "reorder", "reshuffle"],
    "live": ["reside", "dwell", "inhabit", "occupy", "stay", "live", "exist", "survive", "endure", "persist"],
    "stop": ["halt", "cease", "discontinue", "terminate", "end", "finish", "conclude", "wrap up", "shut down", "close"],
    "play": ["perform", "act", "participate", "engage", "take part", "join in", "compete", "contend", "compete", "compete"],
    "stand": ["remain", "stay", "endure", "persist", "continue", "last", "survive", "withstand", "tolerate", "bear"],
    "lose": ["misplace", "lose", "fail to win", "be defeated", "suffer defeat", "be beaten", "be overcome", "be vanquished", "be conquered"],
    "win": ["succeed", "triumph", "prevail", "victory", "win", "win", "win", "win", "win", "win"],
    "fall": ["drop", "descend", "plunge", "tumble", "collapse", "topple", "overturn", "topple over", "fall down", "come down"],
    "sit": ["seat", "sit down", "take a seat", "be seated", "rest", "settle", "perch", "position oneself", "take one's seat"],
    "lie": ["recline", "lie down", "rest", "stretch out", "lie back", "lounge", "relax", "unwind", "recumbent"],
    "learn": ["study", "acquire knowledge", "gain knowledge", "obtain knowledge", "get knowledge", "master", "grasp", "comprehend", "understand"],
    "grow": ["increase", "expand", "develop", "progress", "advance", "mature", "evolve", "flourish", "thrive", "prosper"],
    "open": ["uncover", "reveal", "disclose", "expose", "unveil", "display", "show", "present", "demonstrate", "exhibit"],
    "walk": ["stroll", "stride", "march", "pace", "tread", "step", "proceed", "advance", "progress", "move forward"],
    "write": ["compose", "draft", "pen", "author", "create", "produce", "generate", "formulate", "craft", "write"],
    "read": ["peruse", "scan", "skim", "browse", "examine", "study", "review", "inspect", "analyze", "interpret"],
    "sing": ["vocalize", "chant", "carol", "hum", "trill", "warble", "croon", "serenade", "perform", "sing"],
    "stop": ["halt", "cease", "discontinue", "terminate", "end", "finish", "conclude", "wrap up", "shut down", "close"],
    "talk": ["speak", "communicate", "converse", "discuss", "chat", "gossip", "talk", "talk", "talk", "talk"],
    "sleep": ["rest", "doze", "nap", "slumber", "snooze", "hibernate", "recline", "relax", "unwind", "repose"],
    "wake": ["awaken", "arise", "get up", "rise", "emerge", "appear", "surface", "materialize", "come to", "wake up"],
    "eat": ["consume", "ingest", "devour", "feast on", "partake of", "dine on", "savor", "enjoy", "taste", "sample"],
    "drink": ["consume", "sip", "gulp", "swallow", "quaff", "imbibe", "partake", "indulge", "enjoy", "savor"],
    "laugh": ["chuckle", "giggle", "snicker", "titter", "chortle", "guffaw", "roar with laughter", "burst out laughing", "break into laughter"],
    "cry": ["weep", "sob", "wail", "bawl", "blubber", "snivel", "whimper", "lament", "mourn", "grieve"],
    "love": ["adore", "cherish", "treasure", "value", "appreciate", "esteem", "respect", "honor", "admire", "worship"],
    "hate": ["despise", "loathe", "detest", "abhor", "revile", "scorn", "disdain", "contemn", "execrate", "abominate"],
    "like": ["enjoy", "prefer", "favor", "appreciate", "value", "treasure", "cherish", "admire", "respect", "esteem"],
    "want": ["desire", "wish", "crave", "long for", "yearn for", "aspire to", "hope for", "seek", "pursue", "strive for"],
    "need": ["require", "demand", "necessitate", "call for", "involve", "entail", "obligate", "compel", "force", "impel"],
    "have": ["possess", "own", "hold", "contain", "include", "comprise", "embody", "embrace", "encompass", "incorporate"],
    "do": ["perform", "execute", "carry out", "implement", "accomplish", "achieve", "complete", "fulfill", "conduct", "undertake"],
    "be": ["exist", "live", "occur", "happen", "take place", "transpire", "transpire", "transpire", "transpire", "transpire"],
    "go": ["proceed", "advance", "progress", "continue", "move forward", "journey", "travel", "head", "proceed", "proceed"],
    "come": ["arrive", "approach", "reach", "enter", "appear", "show up", "present", "emerge", "materialize", "surface"]
}

def get_comprehensive_synonyms():
    """Get the comprehensive synonym dictionary"""
    return COMPREHENSIVE_SYNONYMS

def get_synonym_count():
    """Get the total number of words with synonyms"""
    return len(COMPREHENSIVE_SYNONYMS)

def get_total_synonyms():
    """Get the total number of synonym alternatives"""
    total = 0
    for word, synonyms in COMPREHENSIVE_SYNONYMS.items():
        total += len(synonyms)
    return total

if __name__ == "__main__":
    print("🔄 Comprehensive Synonym Dictionary")
    print("=" * 50)
    print(f"📝 Total words with synonyms: {get_synonym_count()}")
    print(f"🔤 Total synonym alternatives: {get_total_synonyms()}")
    print(f"📊 Average synonyms per word: {get_total_synonyms() / get_synonym_count():.1f}")
    print("=" * 50)
    print("✨ Ready for enhanced word replacement!")
