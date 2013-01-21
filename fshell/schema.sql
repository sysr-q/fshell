CREATE TABLE IF NOT EXISTS `fshell` (
    `id` INTEGER PRIMARY KEY,
    `method` varchar(16) NOT NULL, -- The HTTP method they use; GET, POST
    `ip` varchar(15) NOT NULL,     -- The IP address of the offender
    `time` INTEGER NOT NULL,       -- UNIX timestamp of request, in form of: int(time.time())
    
    `agent` TEXT NOT NULL,         -- The full useragent.
    `agent_platform` TEXT NOT NULL,-- User-Agent: platform reported by Flask - request.user_agent.platform
    `agent_browser` TEXT NOT NULL, -- User-Agent: browser reported by Flask - request.user_agent.browser
    `agent_version` TEXT NOT NULL, -- User-Agent: version reported by Flask - request.user_agent.version
    `agent_language` TEXT NOT NULL -- User-Agent: language reported by Flask - request.user_agent.language
);