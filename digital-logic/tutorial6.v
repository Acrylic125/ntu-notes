module dec2to4 (input [1:0] i,  input en,  output [3:0] d);
    wire n0, n1;
    not g1 (n0, i[0]);
    not g2 (n1, i[1]);

    and a1 (d[0], en, n0, n1);
    and a2 (d[1], en, n0, i[1]);
    and a3 (d[2], en, i[0], n1);
    and a4 (d[3], en, i[0], i[1]);
endmodule