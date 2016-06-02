register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' Using TextLoader as (line:chararray);
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' Using TextLoader as (line:chararray);
-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by object column
subjects_match_rdfabout = filter ntriples by subject matches '.*business.*';
clone_subjects = foreach subjects_match_rdfabout generate subject as subject2, predicate as predicate2, object as object2 parallel 50;

subgraph = JOIN subjects_match_rdfabout BY subject, clone_subjects BY subject2; 

unique_subgrph = DISTINCT subgraph;

-- store the results in the folder /user/hadoop/testoutput
store unique_subgrph into '/user/hadoop/testoutput' using PigStorage();

-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_object_ordered into 's3n://superman/example-results';
