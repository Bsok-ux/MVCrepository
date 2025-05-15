using Microsoft.AspNetCore.Mvc;
using System.Linq;
using MyMvcApp.Data;
using System.Threading.Tasks;
using MyMvcApp.Models; 
using Microsoft.EntityFrameworkCore;

namespace MyMvcApp.Controllers  
{
    public class MoviesController : Controller
    {
        private readonly MyMvcAppContext _context;

        public MoviesController(MyMvcAppContext context)
        {
            _context = context;
        }

        public async Task<IActionResult> Index(string searchString)
        {
            var movies = from m in _context.Movie
                         select m;

            if (!string.IsNullOrEmpty(searchString))
            {
                movies = movies.Where(s => s.Title.Contains(searchString));
            }

            return View(await movies.ToListAsync());
        }
    }
}
