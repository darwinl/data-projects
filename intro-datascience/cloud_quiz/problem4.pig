register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' Using TextLoader as (line:chararray);
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-*' Using TextLoader as (line:chararray);
-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by object column
subjects = group ntriples by (subject) PARALLEL 50;

-- flatten the subjects out (because group by produces a tuple of each subject
-- in the first column, and we want each object ot be a string, not a tuple),
-- and count the number of tuples associated with each subject
subject_by_count = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;

counts = group subject_by_count by (count) PARALLEL 50;

x_y_count = foreach counts generate flatten($0), COUNT($1) as count PARALLEL 50;


-- store the results in the folder /user/hadoop/finaloutput
store x_y_count into '/user/hadoop/finaloutput' using PigStorage();

-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_object_ordered into 's3n://superman/example-results';
