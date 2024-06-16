-- Creates an index based on first character of a name
-- The concept is to use prefix indices
CREATE INDEX idx_name_first on names(name(1));
